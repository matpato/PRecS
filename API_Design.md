# Drug Recommendation API Design

## Overview

A Web API that recommends drugs based on a user-provided medical condition, with two ranking strategies:
1. **Recency-based**: Prioritize drugs with more recent reviews
2. **Condition-specific ratings**: Prioritize drugs with highest ratings for the specific condition

---

## API Endpoint Structure

### Base Endpoint
```
GET /api/recommend
```

### Query Parameters

| Parameter | Type | Required | Description | Example |
|-----------|------|----------|-------------|---------|
| `condition` | string | Yes | The disease/diagnosis name | `diabetes` |
| `strategy` | string | No | Ranking strategy: `recency` or `rating` (default: `rating`) | `recency` |

### Example Requests
```
GET /api/recommend?condition=diabetes&strategy=recency
GET /api/recommend?condition=hypertension&strategy=rating
GET /api/recommend?condition=asthma
```

---

## Response Format

### Success Response (200 OK)

```json
{
  "condition": "diabetes",
  "strategy": "recency",
  "total_reviews": 150,
  "recommendations": [
    {
      "drug_name": "metformin",
      "drug_name_generic": "metformin hydrochloride",
      "avg_rating": 8.5,
      "num_reviews": 150,
      "most_recent_review": "2024-01-15",
      "oldest_review": "2020-03-10",
      "weighted_score": 8.7,
      "useful_count_total": 420
    },
    {
      "drug_name": "insulin",
      "drug_name_generic": "insulin regular",
      "avg_rating": 7.8,
      "num_reviews": 98,
      "most_recent_review": "2024-01-10",
      "oldest_review": "2019-11-22",
      "weighted_score": 8.1,
      "useful_count_total": 285
    }
  ]
}
```

### Error Response (404 Not Found)

```json
{
  "error": "No drugs found for the specified condition",
  "condition": "unknown_disease"
}
```

### Error Response (400 Bad Request)

```json
{
  "error": "Invalid strategy parameter",
  "valid_options": ["recency", "rating"]
}
```

---

## Ranking Strategies

### 1. Recency Strategy

**Algorithm**: Weight recent reviews higher using exponential decay

```python
weighted_score = rating × e^(-λ × age_in_days)
```

- **λ (lambda)**: Decay parameter (e.g., 0.001)
- **age_in_days**: Days since the review was posted
- Recent reviews contribute more to the final score

**Sorting**: Descending by `weighted_score`

---

### 2. Condition-Specific Rating Strategy

**Algorithm**: Aggregate ratings for drugs prescribed for the specific condition

```python
avg_rating = sum(ratings) / count(ratings)
# Optional: Weight by useful_count
weighted_avg = sum(rating × useful_count) / sum(useful_count)
```

**Sorting**: Descending by `avg_rating` or `weighted_avg`

---

## Data Considerations

### Dataset Structure
- **Rating Scale**: 1-10
- **Rating Distribution**: U-shaped (more 1-2 and 7-10 ratings)
- **Features Available**:
  - `diagnosis` / `clean_diagnosis`: Disease/condition
  - `drug` / `drug_name_generic`: Drug names
  - `rating`: User rating (1-10)
  - `usefulcount`: Helpfulness votes
  - `datetime`: Review timestamp

### Filtering Logic
1. Filter dataset by exact condition match (or fuzzy match)
2. Group by drug name
3. Calculate aggregate metrics (avg_rating, num_reviews, etc.)
4. Apply selected ranking strategy
5. Return top N recommendations (e.g., top 10)

---

## Implementation Questions

Before building the API, consider:

1. **Framework**: FastAPI, Flask, or Django REST Framework?
2. **Database**: 
   - Load CSV into PostgreSQL/MySQL for scalability?
   - Use SQLite for simplicity?
   - Keep in-memory (Pandas DataFrame) for prototyping?
3. **Condition Matching**:
   - Exact match only?
   - Fuzzy search (e.g., "diabetes" matches "diabetes type 2")?
   - Case-insensitive?
4. **Response Limits**: How many recommendations to return? (default: 10)
5. **Caching**: Cache results for frequently queried conditions?

---

## Future Enhancements

- **Pagination**: Support `limit` and `offset` parameters
- **Filtering**: Add filters for `drug_type`, `route`, `gender`, etc.
- **Hybrid Strategy**: Combine recency and rating with weighted formula
- **Confidence Scores**: Include confidence intervals based on `num_reviews`
- **User Preferences**: Allow users to specify weights for recency vs. rating
- **Additional Endpoints**:
  - `GET /api/drugs/{drug_name}` - Get details for a specific drug
  - `GET /api/conditions` - List all available conditions
  - `POST /api/feedback` - Submit new ratings

---

## Example Use Cases

### Use Case 1: Patient Looking for Effective Treatment
```
GET /api/recommend?condition=migraine&strategy=rating
```
→ Returns drugs with highest average ratings for migraine

### Use Case 2: Doctor Wanting Latest Treatment Trends
```
GET /api/recommend?condition=depression&strategy=recency
```
→ Returns drugs that have been positively reviewed recently

### Use Case 3: Default Recommendation
```
GET /api/recommend?condition=arthritis
```
→ Returns drugs sorted by condition-specific ratings (default strategy)

---

## Notes

- **U-shaped Rating Distribution**: Consider filtering or weighting to handle polarized ratings
- **Data Quality**: Ensure `clean_diagnosis` field is used for consistent condition matching
- **Privacy**: Ensure no patient identifiable information (PII) is exposed through the API
- **Rate Limiting**: Implement API rate limiting to prevent abuse