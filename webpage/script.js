function updateSlider(spanId, value) {
    document.getElementById(spanId).textContent = value;
}

// NEW: Fetches stats and updates slider MAX values immediately
async function updateSliders(condition) {
    if (!condition) return;
    
    try {
        const response = await fetch('http://127.0.0.1:8000/api/condition_stats', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ condition: condition })
        });
        const data = await response.json();
        const maxReviews = data.max_reviews;
        
        if (maxReviews > 0) {
            // 1. Update Max Reviews Slider (Display/Cap)
            const maxInput = document.getElementById("maxInput");
            if (maxInput) {
                maxInput.max = maxReviews;
                maxInput.value = maxReviews; // Set to max as requested
                if(maxInput.nextElementSibling) maxInput.nextElementSibling.value = maxReviews;
            }

            // 2. Update Minimum Reviews Slider (Filter)
            const minInput = document.getElementById("minReviewsInput");
            if (minInput) {
                minInput.max = maxReviews; // Set SAME max as requested
                
                // Ensure current value doesn't exceed new max
                if (parseInt(minInput.value) > maxReviews) {
                    minInput.value = maxReviews;
                }
                
                if(minInput.nextElementSibling) minInput.nextElementSibling.value = minInput.value;
            }
        }
    } catch (error) {
        console.error("Error fetching condition stats:", error);
    }
}

async function getConditions() {
    const text = document.getElementById("symptomInput").value;
    const aiSelect = document.getElementById("conditionInput");

    if (text.length < 3) {
        aiSelect.innerHTML = '<option value="">Waiting for symptoms...</option>';
        return;
    }

    try {
        const response = await fetch('http://127.0.0.1:8000/api/predict_condition', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ text: text })
        });
        const data = await response.json();
        
        aiSelect.innerHTML = "";
        if (data.conditions.length === 0) {
            aiSelect.innerHTML = '<option value="">No specific condition detected</option>';
        } else {
            data.conditions.forEach(cond => {
                const opt = document.createElement("option");
                opt.value = cond;
                opt.text = "" + cond;
                opt.selected = true; 
                aiSelect.add(opt);
            });
            
            // Trigger slider update for the first detected condition
            updateSliders(data.conditions[0]);
        }
    } catch (error) {
        console.error("Errore API:", error);
    }
}

async function getRecommendations() {
    let condition = document.getElementById("conditionInput").value;
    if (!condition) {
        condition = document.getElementById("diseaseInput").value;
    }

    const limit = document.getElementById("recommendationsInput").value || 5;
    const model = document.getElementById("modelInput").value;
    const minReviews = document.getElementById("minReviewsInput").value;
    const recencyPeriod = document.getElementById("recencyPeriodInput").value;

    if (!condition) {
        alert("Please describe symptoms or select a disease manually.");
        return;
    }

    try {
        const response = await fetch('http://127.0.0.1:8000/api/recommend', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ 
                condition: condition, 
                limit: parseInt(limit),
                model: model,
                min_reviews: parseInt(minReviews),
                time_filter: recencyPeriod
            })
        });

        const data = await response.json();

        // 2. Confidence: Show the confidence of the Top 1 Drug and Disable it
        const confInput = document.getElementById("confidenceInput");
        if (data.results && data.results.length > 0) {
            const topConfidence = Math.round(data.results[0].confidence);
            confInput.value = topConfidence;
            if(confInput.nextElementSibling) {
                confInput.nextElementSibling.value = topConfidence + "%";
            }
        } else {
            confInput.value = 0;
            if(confInput.nextElementSibling) confInput.nextElementSibling.value = "0%";
        }
        confInput.disabled = true;

        renderTable(data.results);

    } catch (error) {
        console.error("Errore fetch:", error);
        alert("Server error. Check console.");
    }
}

function renderTable(results) {
    const tableBody = document.querySelector("#resultsArea tbody");
    tableBody.innerHTML = ""; 

    if (!results || results.length === 0) {
        tableBody.innerHTML = `<tr><td colspan="7" style="text-align:center; padding: 20px;">No drugs found matching criteria.</td></tr>`;
        return;
    }

    results.forEach(item => {
        const row = document.createElement("tr");
        
        let barColor = '#e74c3c'; 
        if(item.confidence > 50) barColor = '#f1c40f'; 
        if(item.confidence > 80) barColor = '#2ecc71'; 

        row.innerHTML = `
            <td>#${item.rank}</td>
            <td><b>${item.drug}</b></td>
            <td>${item.condition}</td>
            <td>${item.score}</td>
            <td style="font-weight:bold; color: #166534; background-color: #dcfce7;">${item.weighted_rating}</td>
            <td>
                <div style="display:flex; align-items:center; gap:10px;">
                    <span>${item.confidence}%</span>
                    <div class="confidence-container">
                        <div class="confidence-bar" style="width: ${item.confidence}%; background-color: ${barColor};"></div>
                    </div>
                </div>
            </td>
            <td>${item.sample_size}</td>
        `;
        tableBody.appendChild(row);
    });
}