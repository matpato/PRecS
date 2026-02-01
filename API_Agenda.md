# PyPI Package + Web API Development Project: Drug Recommendation System
## 3-4 Week Agenda for Erasmus Students

---

## **Project Overview**

**Objective**: Develop a professional Python package for drug recommendation based on disease-drug-rating analysis that can be:
1. **Published to PyPI** for public use by researchers and developers
2. **Deployed as a Web API** for integration with web and mobile applications

**Dual-Purpose Design**:
```python
# As a Python library (PyPI package)
from drug_recommender import DrugRecommender, RatingAnalyzer

recommender = DrugRecommender()
results = recommender.recommend_by_condition("diabetes", strategy="recency")
ratings = RatingAnalyzer.get_drug_ratings("metformin")

# As a Web API (FastAPI service)
# GET /api/v1/recommend?condition=diabetes&strategy=recency
# GET /api/v1/drugs/{drug_name}/ratings
```

**Domain**: Medical/Pharmaceutical drug recommendation system using collaborative filtering and rating analysis.

**Key Deliverables**:
- ✅ Python package installable via `pip install drug-recommender`
- ✅ RESTful Web API for web/mobile integration
- ✅ Comprehensive documentation (PyPI + API docs)
- ✅ Example notebooks and tutorials
- ✅ Docker deployment for the API

---

## **Week 1: Domain Understanding & Package Architecture**

### **Day 1-2: Domain Analysis & Requirements**

**Objectives**:
- Understand the pharmaceutical domain and recommendation systems
- Define package scope and API requirements
- Plan PyPI package structure

**Tasks**:

1. **Study the Domain**:
   - Drug review systems and rating methodologies
   - Recommendation systems (collaborative filtering, content-based)
   - Medical condition classification (ICD-11)
   - Statistical considerations for medical data
   - Ethics and privacy in medical software

2. **Analyze ratingAnalyzer.ipynb**:
   - Core functionality mapping:
     * Data loading and cleaning
     * Duplicate detection
     * Condition classification
     * Statistical rating calculations
     * Rating aggregation and weighting
     * Recency-based scoring
     * Visualization generation
   
3. **Define Package Scope**:
   
   **Core Library Features**:
   ```python
   # Main functionality to expose
   - DrugRecommender: Main recommendation class
   - RatingAnalyzer: Rating aggregation and statistics
   - ConditionMatcher: Medical condition matching/search
   - RecencyScorer: Time-weighted scoring
   - DataValidator: Input validation and cleaning
   - Visualizer: Generate analysis plots
   ```

   **Web API Features**:
   ```
   - RESTful endpoints wrapping library functions
   - Request/response validation
   - Authentication and rate limiting
   - Async processing for large datasets
   - OpenAPI/Swagger documentation
   ```

4. **PyPI Package Requirements**:
   - Clear, focused functionality
   - Minimal dependencies
   - Well-documented API
   - Comprehensive examples
   - Semantic versioning
   - Open-source license (MIT recommended)

**Deliverable**: 
- Requirements document
- Package design specification
- API endpoint specifications
- PyPI metadata plan

---

### **Day 3-5: Package Structure & Architecture**

**Objectives**:
- Design package architecture
- Set up project structure for PyPI
- Configure development environment

**Tasks**:

1. **Python Package Structure** (PyPI-ready):
   ```
   drug-recommender/
   ├── src/
   │   └── drug_recommender/
   │       ├── __init__.py              # Package initialization
   │       ├── __version__.py           # Version info
   │       ├── core/
   │       │   ├── __init__.py
   │       │   ├── recommender.py       # Main DrugRecommender class
   │       │   ├── ratings.py           # RatingAnalyzer
   │       │   ├── conditions.py        # ConditionMatcher
   │       │   ├── recency.py           # RecencyScorer
   │       │   └── statistics.py        # Statistical functions
   │       ├── data/
   │       │   ├── __init__.py
   │       │   ├── validator.py         # Data validation
   │       │   ├── cleaner.py           # Data cleaning
   │       │   └── loader.py            # Data loading utilities
   │       ├── utils/
   │       │   ├── __init__.py
   │       │   ├── text_processing.py   # Text normalization
   │       │   ├── similarity.py        # Condition similarity
   │       │   └── constants.py         # Constants and configs
   │       ├── viz/
   │       │   ├── __init__.py
   │       │   └── plots.py             # Visualization functions
   │       └── exceptions.py            # Custom exceptions
   │
   ├── api/                              # Web API (separate from core package)
   │   ├── __init__.py
   │   ├── main.py                      # FastAPI application
   │   ├── config.py
   │   ├── models/
   │   │   ├── __init__.py
   │   │   └── schemas.py               # Pydantic models
   │   ├── routers/
   │   │   ├── __init__.py
   │   │   ├── recommendations.py       # Recommendation endpoints
   │   │   ├── drugs.py                 # Drug info endpoints
   │   │   └── health.py                # Health check
   │   └── dependencies.py              # API dependencies
   │
   ├── tests/
   │   ├── __init__.py
   │   ├── test_recommender.py
   │   ├── test_ratings.py
   │   ├── test_conditions.py
   │   ├── test_recency.py
   │   └── test_api.py
   │
   ├── examples/
   │   ├── basic_usage.py
   │   ├── advanced_analysis.ipynb
   │   ├── api_integration.py
   │   └── sample_data/
   │
   ├── docs/
   │   ├── index.md
   │   ├── installation.md
   │   ├── quickstart.md
   │   ├── api_reference.md
   │   └── contributing.md
   │
   ├── docker/
   │   ├── Dockerfile
   │   └── docker-compose.yml
   │
   ├── .github/
   │   └── workflows/
   │       ├── tests.yml                # CI/CD pipeline
   │       └── publish.yml              # PyPI publishing
   │
   ├── setup.py                         # Package setup (legacy)
   ├── pyproject.toml                   # Modern Python packaging
   ├── requirements.txt                 # Core dependencies
   ├── requirements-dev.txt             # Development dependencies
   ├── requirements-api.txt             # API-specific dependencies
   ├── README.md                        # Main documentation
   ├── LICENSE                          # MIT License
   ├── MANIFEST.in                      # Include non-Python files
   └── .gitignore
   ```

2. **pyproject.toml Configuration**:
   ```toml
   [build-system]
   requires = ["setuptools>=61.0", "wheel"]
   build-backend = "setuptools.build_meta"

   [project]
   name = "drug-recommender"
   version = "0.1.0"
   description = "A comprehensive toolkit for recommending drugs based on disease-drug-rating analysis"
   readme = "README.md"
   authors = [
       {name = "Erasmus Student Team", email = "team@university.edu"}
   ]
   license = {text = "MIT"}
   classifiers = [
       "Development Status :: 3 - Alpha",
       "Intended Audience :: Healthcare Industry",
       "Intended Audience :: Science/Research",
       "License :: OSI Approved :: MIT License",
       "Programming Language :: Python :: 3",
       "Programming Language :: Python :: 3.9",
       "Programming Language :: Python :: 3.10",
       "Programming Language :: Python :: 3.11",
       "Topic :: Scientific/Engineering :: Medical Science Apps.",
       "Topic :: Scientific/Engineering :: Information Analysis",
   ]
   keywords = ["drug-recommendation", "healthcare", "pharmaceutical", "collaborative-filtering", "rating-analysis"]
   dependencies = [
       "pandas>=2.0.0",
       "numpy>=1.24.0",
       "scipy>=1.10.0",
       "scikit-learn>=1.3.0",
       "matplotlib>=3.7.0",
       "seaborn>=0.12.0",
   ]
   requires-python = ">=3.9"

   [project.optional-dependencies]
   api = [
       "fastapi>=0.109.0",
       "uvicorn[standard]>=0.27.0",
       "pydantic>=2.5.0",
       "python-multipart>=0.0.6",
   ]
   dev = [
       "pytest>=7.4.0",
       "pytest-cov>=4.1.0",
       "black>=23.0.0",
       "flake8>=6.0.0",
       "mypy>=1.7.0",
       "sphinx>=7.0.0",
   ]

   [project.urls]
   Homepage = "https://github.com/matpato/drug-recommender"
   Documentation = "https://drug-recommender.readthedocs.io"
   Repository = "https://github.com/matpato/drug-recommender"
   "Bug Tracker" = "https://github.com/matpato/drug-recommender/issues"
   ```

3. **Architecture Principles**:
   
   **Separation of Concerns**:
   - Core library: Pure Python logic, no web dependencies
   - API layer: Thin wrapper around core library
   - Clear interfaces between components
   
   **Design Patterns**:
   - Factory pattern for recommender creation
   - Strategy pattern for different scoring methods (recency, rating)
   - Singleton for configuration management
   
   **Dependency Management**:
   - Core: Only essential scientific libraries (pandas, numpy, scipy, sklearn)
   - API extras: FastAPI dependencies installed separately
   - Development extras: Testing and documentation tools

4. **Development Environment Setup**:
   ```bash
   # Create virtual environment
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   
   # Install in development mode
   pip install -e ".[dev,api]"
   
   # Setup pre-commit hooks
   pre-commit install
   ```

**Deliverable**: 
- Complete package structure
- pyproject.toml configured
- Development environment ready
- Git repository initialized

---

## **Week 2: Core Library Implementation**

### **Day 1-3: Core Recommendation Engine**

**Objectives**:
- Implement main recommendation logic
- Build rating aggregation system
- Create condition matching functionality

**Tasks**:

1. **DrugRecommender Class** (`core/recommender.py`):
   ```python
   class DrugRecommender:
       """
       Main class for drug recommendations based on condition and strategy.
       
       Example:
           >>> recommender = DrugRecommender(data_path="reviews.csv")
           >>> results = recommender.recommend(
           ...     condition="diabetes",
           ...     strategy="recency",
           ...     top_n=10
           ... )
       """
       
       def __init__(self, data_path: str = None, dataframe: pd.DataFrame = None):
           """Initialize recommender with data source."""
           
       def recommend(
           self,
           condition: str,
           strategy: str = "rating",
           top_n: int = 10,
           **kwargs
       ) -> List[DrugRecommendation]:
           """
           Recommend drugs for a given condition.
           
           Args:
               condition: Disease/condition name
               strategy: "rating" or "recency"
               top_n: Number of recommendations to return
               
           Returns:
               List of DrugRecommendation objects
           """
           
       def _filter_by_condition(self, condition: str) -> pd.DataFrame:
           """Filter reviews by condition."""
           
       def _aggregate_ratings(self, filtered_df: pd.DataFrame) -> pd.DataFrame:
           """Aggregate ratings by drug."""
           
       def _apply_strategy(
           self, 
           aggregated_df: pd.DataFrame,
           strategy: str
       ) -> pd.DataFrame:
           """Apply scoring strategy."""
   ```

2. **RatingAnalyzer Class** (`core/ratings.py`):
   ```python
   class RatingAnalyzer:
       """
       Statistical analysis of drug ratings.
       
       Handles:
       - Rating aggregation (mean, median, weighted)
       - Distribution analysis
       - Confidence intervals
       - Useful count weighting
       """
       
       @staticmethod
       def calculate_weighted_rating(
           ratings: pd.Series,
           useful_counts: pd.Series
       ) -> float:
           """Calculate weighted average rating."""
           
       @staticmethod
       def calculate_confidence_interval(
           ratings: pd.Series,
           confidence: float = 0.95
       ) -> Tuple[float, float]:
           """Calculate confidence interval for ratings."""
           
       @staticmethod
       def get_rating_statistics(ratings: pd.Series) -> Dict:
           """Get comprehensive rating statistics."""
   ```

3. **ConditionMatcher Class** (`core/conditions.py`):
   ```python
   class ConditionMatcher:
       """
       Match and normalize medical conditions.
       
       Features:
       - Exact matching
       - Fuzzy matching
       - Synonym handling
       - Case-insensitive search
       """
       
       def __init__(self, conditions: List[str]):
           """Initialize with list of known conditions."""
           
       def match(
           self,
           query: str,
           method: str = "exact",
           threshold: float = 0.8
       ) -> List[str]:
           """
           Match query to known conditions.
           
           Args:
               query: User input condition
               method: "exact", "fuzzy", or "contains"
               threshold: Similarity threshold for fuzzy matching
               
           Returns:
               List of matched condition names
           """
           
       def normalize(self, condition: str) -> str:
           """Normalize condition name."""
   ```

4. **RecencyScorer Class** (`core/recency.py`):
   ```python
   class RecencyScorer:
       """
       Time-weighted scoring for recommendations.
       
       Uses exponential decay: score = rating × e^(-λ × age_in_days)
       """
       
       def __init__(self, decay_rate: float = 0.001):
           """
           Initialize with decay rate.
           
           Args:
               decay_rate: Lambda parameter for exponential decay
           """
           
       def calculate_recency_score(
           self,
           rating: float,
           review_date: datetime,
           reference_date: datetime = None
       ) -> float:
           """Calculate time-weighted score."""
           
       def score_dataframe(
           self,
           df: pd.DataFrame,
           rating_col: str = "rating",
           date_col: str = "datetime"
       ) -> pd.Series:
           """Apply recency scoring to entire dataframe."""
   ```

**Deliverable**: 
- Core classes implemented with docstrings
- Unit tests for each class (>70% coverage)
- Type hints throughout

---

### **Day 4-5: Data Processing & Utilities**

**Objectives**:
- Implement data validation and cleaning
- Create utility functions
- Build visualization tools

**Tasks**:

1. **DataValidator Class** (`data/validator.py`):
   ```python
   class DataValidator:
       """
       Validate drug review data.
       
       Checks:
       - Required columns present
       - Data types correct
       - Rating range (1-10)
       - Date format valid
       - No critical missing values
       """
       
       @staticmethod
       def validate_dataframe(df: pd.DataFrame) -> ValidationResult:
           """Validate input dataframe."""
           
       @staticmethod
       def validate_rating(rating: float) -> bool:
           """Check if rating is in valid range."""
   ```

2. **DataCleaner Class** (`data/cleaner.py`):
   ```python
   class DataCleaner:
       """
       Clean and preprocess drug review data.
       
       Operations:
       - Remove duplicates
       - Handle missing values
       - Normalize text
       - Parse dates
       - Filter outliers
       """
       
       def clean(self, df: pd.DataFrame) -> pd.DataFrame:
           """Apply all cleaning operations."""
           
       def remove_duplicates(self, df: pd.DataFrame) -> pd.DataFrame:
           """Remove duplicate reviews."""
           
       def handle_missing(self, df: pd.DataFrame) -> pd.DataFrame:
           """Handle missing values."""
   ```

3. **Visualization Tools** (`viz/plots.py`):
   ```python
   class RecommendationVisualizer:
       """
       Create visualizations for drug recommendations.
       
       Plots:
       - Rating distribution
       - Top recommended drugs
       - Recency trends
       - Confidence intervals
       """
       
       @staticmethod
       def plot_recommendations(
           recommendations: List[DrugRecommendation],
           title: str = "Top Drug Recommendations"
       ) -> plt.Figure:
           """Plot bar chart of recommendations."""
           
       @staticmethod
       def plot_rating_distribution(
           drug_name: str,
           ratings: pd.Series
       ) -> plt.Figure:
           """Plot rating distribution for a drug."""
           
       @staticmethod
       def plot_recency_trend(
           df: pd.DataFrame,
           drug_name: str
       ) -> plt.Figure:
           """Plot rating trend over time."""
   ```

4. **Text Processing Utilities** (`utils/text_processing.py`):
   ```python
   def normalize_condition(condition: str) -> str:
       """Normalize condition text."""
       
   def calculate_similarity(text1: str, text2: str) -> float:
       """Calculate text similarity score."""
       
   def tokenize(text: str) -> List[str]:
       """Tokenize medical condition text."""
   ```

**Deliverable**: 
- All utility modules implemented
- Comprehensive unit tests
- Example usage scripts

---

## **Week 3: Web API Development**

### **Day 1-3: FastAPI Implementation**

**Objectives**:
- Build RESTful API endpoints
- Implement request/response models
- Add API documentation

**Tasks**:

1. **API Models** (`api/models/schemas.py`):
   ```python
   from pydantic import BaseModel, Field
   from typing import List, Optional
   from datetime import datetime
   
   class RecommendationRequest(BaseModel):
       """Request model for drug recommendations."""
       condition: str = Field(..., description="Medical condition/disease")
       strategy: str = Field("rating", description="Scoring strategy: 'rating' or 'recency'")
       top_n: int = Field(10, ge=1, le=50, description="Number of recommendations")
       
   class DrugRecommendationResponse(BaseModel):
       """Response model for a single drug recommendation."""
       drug_name: str
       drug_name_generic: str
       avg_rating: float
       num_reviews: int
       most_recent_review: datetime
       oldest_review: datetime
       weighted_score: float
       useful_count_total: int
       confidence_interval: Optional[tuple[float, float]] = None
       
   class RecommendationsResponse(BaseModel):
       """Response model for recommendation endpoint."""
       condition: str
       strategy: str
       total_reviews: int
       recommendations: List[DrugRecommendationResponse]
       
   class ErrorResponse(BaseModel):
       """Error response model."""
       error: str
       details: Optional[str] = None
   ```

2. **Main API Application** (`api/main.py`):
   ```python
   from fastapi import FastAPI, HTTPException
   from fastapi.middleware.cors import CORSMiddleware
   
   app = FastAPI(
       title="Drug Recommender API",
       description="API for drug recommendations based on condition-drug-rating analysis",
       version="0.1.0",
       docs_url="/docs",
       redoc_url="/redoc"
   )
   
   # CORS middleware
   app.add_middleware(
       CORSMiddleware,
       allow_origins=["*"],
       allow_credentials=True,
       allow_methods=["*"],
       allow_headers=["*"],
   )
   
   # Include routers
   from api.routers import recommendations, drugs, health
   app.include_router(recommendations.router, prefix="/api/v1")
   app.include_router(drugs.router, prefix="/api/v1")
   app.include_router(health.router, prefix="/api/v1")
   ```

3. **Recommendation Router** (`api/routers/recommendations.py`):
   ```python
   from fastapi import APIRouter, HTTPException, Query
   from api.models.schemas import RecommendationsResponse, ErrorResponse
   from drug_recommender import DrugRecommender
   
   router = APIRouter(tags=["recommendations"])
   
   # Initialize recommender (load data once at startup)
   recommender = DrugRecommender(data_path="data/drug_reviews.csv")
   
   @router.get(
       "/recommend",
       response_model=RecommendationsResponse,
       responses={404: {"model": ErrorResponse}}
   )
   async def get_recommendations(
       condition: str = Query(..., description="Medical condition"),
       strategy: str = Query("rating", description="Scoring strategy"),
       top_n: int = Query(10, ge=1, le=50, description="Number of results")
   ):
       """
       Get drug recommendations for a medical condition.
       
       **Strategies:**
       - `rating`: Sort by highest average rating
       - `recency`: Weight recent reviews higher
       """
       try:
           results = recommender.recommend(
               condition=condition,
               strategy=strategy,
               top_n=top_n
           )
           
           if not results:
               raise HTTPException(
                   status_code=404,
                   detail=f"No drugs found for condition: {condition}"
               )
               
           return {
               "condition": condition,
               "strategy": strategy,
               "total_reviews": sum(r.num_reviews for r in results),
               "recommendations": results
           }
           
       except Exception as e:
           raise HTTPException(status_code=500, detail=str(e))
   ```

4. **Drug Info Router** (`api/routers/drugs.py`):
   ```python
   from fastapi import APIRouter, HTTPException
   
   router = APIRouter(tags=["drugs"])
   
   @router.get("/drugs/{drug_name}/ratings")
   async def get_drug_ratings(drug_name: str):
       """Get rating information for a specific drug."""
       
   @router.get("/drugs/{drug_name}/conditions")
   async def get_drug_conditions(drug_name: str):
       """Get conditions this drug is used for."""
       
   @router.get("/conditions")
   async def list_conditions():
       """List all available medical conditions in the database."""
   ```

5. **Health Check Router** (`api/routers/health.py`):
   ```python
   from fastapi import APIRouter
   
   router = APIRouter(tags=["health"])
   
   @router.get("/health")
   async def health_check():
       """API health check endpoint."""
       return {
           "status": "healthy",
           "version": "0.1.0",
           "data_loaded": True
       }
   ```

**Deliverable**: 
- Complete FastAPI implementation
- All endpoints functional
- OpenAPI documentation auto-generated
- API tests written

---

### **Day 4-5: API Testing & Documentation**

**Objectives**:
- Write comprehensive API tests
- Create API usage documentation
- Test error handling

**Tasks**:

1. **API Tests** (`tests/test_api.py`):
   ```python
   from fastapi.testclient import TestClient
   from api.main import app
   
   client = TestClient(app)
   
   def test_health_check():
       response = client.get("/api/v1/health")
       assert response.status_code == 200
       assert response.json()["status"] == "healthy"
   
   def test_get_recommendations():
       response = client.get(
           "/api/v1/recommend",
           params={"condition": "diabetes", "strategy": "rating"}
       )
       assert response.status_code == 200
       data = response.json()
       assert "recommendations" in data
       assert len(data["recommendations"]) > 0
   
   def test_invalid_strategy():
       response = client.get(
           "/api/v1/recommend",
           params={"condition": "diabetes", "strategy": "invalid"}
       )
       assert response.status_code in [400, 422]
   
   def test_condition_not_found():
       response = client.get(
           "/api/v1/recommend",
           params={"condition": "unknown_disease_xyz"}
       )
       assert response.status_code == 404
   ```

2. **API Documentation** (`docs/api_reference.md`):
   - Document all endpoints
   - Include request/response examples
   - Add authentication info (if applicable)
   - Explain error codes
   - Provide curl examples

3. **Integration Testing**:
   - Test end-to-end workflows
   - Performance testing
   - Load testing (optional)

**Deliverable**: 
- Complete API test suite
- API documentation
- Performance benchmarks

---

## **Week 4: Packaging, Deployment & Documentation**

### **Day 1-2: PyPI Package Preparation**

**Objectives**:
- Finalize package for PyPI publication
- Complete documentation
- Test installation process

**Tasks**:

1. **README.md Enhancement**:
   ```markdown
   # Drug Recommender
   
   A Python library and API for recommending drugs based on disease-drug-rating analysis.
   
   ## Features
   
   - 🎯 Intelligent drug recommendations based on ratings
   - ⏰ Recency-weighted scoring for latest trends
   - 📊 Statistical rating analysis
   - 🔍 Flexible condition matching
   - 🚀 REST API for easy integration
   - 📦 Easy installation via pip
   
   ## Installation
   
   ```bash
   # Basic installation
   pip install drug-recommender
   
   # With API support
   pip install drug-recommender[api]
   ```
   
   ## Quick Start
   
   ### As a Library
   
   ```python
   from drug_recommender import DrugRecommender
   
   # Initialize recommender
   recommender = DrugRecommender(data_path="reviews.csv")
   
   # Get recommendations
   results = recommender.recommend(
       condition="diabetes",
       strategy="recency",
       top_n=10
   )
   
   # Print results
   for drug in results:
       print(f"{drug.drug_name}: {drug.weighted_score:.2f}")
   ```
   
   ### As an API
   
   ```bash
   # Start server
   python -m drug_recommender.api
   
   # Make request
   curl "http://localhost:8000/api/v1/recommend?condition=diabetes&strategy=recency"
   ```
   
   ## Documentation
   
   Full documentation: https://drug-recommender.readthedocs.io
   
   ## License
   
   MIT License - see LICENSE file
   ```

2. **Package Building**:
   ```bash
   # Install build tools
   pip install build twine
   
   # Build package
   python -m build
   
   # Check package
   twine check dist/*
   
   # Test on TestPyPI first
   twine upload --repository testpypi dist/*
   
   # Install and test
   pip install --index-url https://test.pypi.org/simple/ drug-recommender
   ```

3. **Documentation Website** (using Sphinx):
   ```bash
   # Setup Sphinx
   cd docs
   sphinx-quickstart
   
   # Build docs
   make html
   
   # Deploy to Read the Docs
   ```

**Deliverable**: 
- Package ready for PyPI
- Complete documentation
- Installation tested

---

### **Day 3-4: Docker Deployment**

**Objectives**:
- Create Docker containers
- Deploy API with Docker Compose
- Test production deployment

**Tasks**:

1. **Dockerfile** (`docker/Dockerfile`):
   ```dockerfile
   FROM python:3.11-slim
   
   WORKDIR /app
   
   # Install dependencies
   COPY requirements.txt requirements-api.txt ./
   RUN pip install --no-cache-dir -r requirements.txt -r requirements-api.txt
   
   # Copy application
   COPY . .
   
   # Install package
   RUN pip install -e .
   
   # Expose API port
   EXPOSE 8000
   
   # Run API
   CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
   ```

2. **Docker Compose** (`docker/docker-compose.yml`):
   ```yaml
   version: '3.8'
   
   services:
     api:
       build:
         context: ..
         dockerfile: docker/Dockerfile
       ports:
         - "8000:8000"
       volumes:
         - ../data:/app/data:ro
       environment:
         - DATA_PATH=/app/data/drug_reviews.csv
       restart: unless-stopped
       healthcheck:
         test: ["CMD", "curl", "-f", "http://localhost:8000/api/v1/health"]
         interval: 30s
         timeout: 10s
         retries: 3
   ```

3. **Production Testing**:
   ```bash
   # Build and run
   docker-compose up -d
   
   # Test health
   curl http://localhost:8000/api/v1/health
   
   # Test recommendation
   curl "http://localhost:8000/api/v1/recommend?condition=diabetes"
   
   # View logs
   docker-compose logs -f
   ```

**Deliverable**: 
- Docker images built
- API running in containers
- Production deployment guide

---

### **Day 5: Final Demo & Presentation**

**Objectives**:
- Publish to PyPI
- Create demo materials
- Prepare final presentation

**Tasks**:

1. **PyPI Publication**:
   ```bash
   # Final build
   python -m build
   
   # Upload to PyPI
   twine upload dist/*
   
   # Verify installation
   pip install drug-recommender
   ```

2. **GitHub Repository**:
   - Push all code
   - Create releases
   - Setup CI/CD workflows
   - Add badges (build status, coverage, PyPI version)

3. **Demo Script** (`examples/demo.py`):
   ```python
   """
   Complete demo of drug-recommender package.
   """
   from drug_recommender import DrugRecommender
   from drug_recommender.viz import RecommendationVisualizer
   
   def main():
       print("🎯 Drug Recommender Demo")
       print("=" * 50)
       
       # Initialize
       print("\n1. Loading data...")
       recommender = DrugRecommender(data_path="data/sample_reviews.csv")
       
       # Rating-based recommendations
       print("\n2. Getting rating-based recommendations for diabetes...")
       results = recommender.recommend(
           condition="diabetes",
           strategy="rating",
           top_n=5
       )
       
       print("\nTop 5 Drugs by Rating:")
       for i, drug in enumerate(results, 1):
           print(f"{i}. {drug.drug_name}")
           print(f"   Rating: {drug.avg_rating:.1f}/10")
           print(f"   Reviews: {drug.num_reviews}")
           print()
       
       # Recency-based recommendations
       print("\n3. Getting recency-based recommendations...")
       results = recommender.recommend(
           condition="diabetes",
           strategy="recency",
           top_n=5
       )
       
       print("\nTop 5 Drugs by Recency:")
       for i, drug in enumerate(results, 1):
           print(f"{i}. {drug.drug_name}")
           print(f"   Weighted Score: {drug.weighted_score:.2f}")
           print(f"   Most Recent: {drug.most_recent_review.date()}")
           print()
       
       # Visualization
       print("\n4. Generating visualization...")
       viz = RecommendationVisualizer()
       fig = viz.plot_recommendations(results)
       fig.savefig("recommendations.png")
       print("   Saved to: recommendations.png")
       
       print("\n✅ Demo complete!")
   
   if __name__ == "__main__":
       main()
   ```
   
   **B. API Demo**:
   ```bash
   # Start API
   uvicorn api.main:app --reload
   
   # Demo requests
   curl -X GET "http://localhost:8000/api/v1/recommend?condition=diabetes&strategy=recency"
   
   curl -X GET "http://localhost:8000/api/v1/drugs/metformin/ratings"
   
   curl -X GET "http://localhost:8000/api/v1/conditions"
   ```

4. **Presentation Materials**:
   - Create PowerPoint/PDF presentation covering:
     * Project overview
     * Technical architecture
     * PyPI package usage
     * API demonstration
     * Recommendation algorithms
     * Use cases and applications
     * Future enhancements
   
5. **Video Tutorial** (Optional):
   - Screen recording showing:
     * Package installation
     * Basic usage
     * API usage
     * Real-world example

6. **Handover Documentation**:
   ```markdown
   # Project Handover Document
   
   ## Overview
   Drug Recommender - PyPI package and Web API for pharmaceutical recommendation system
   
   ## Repository
   - GitHub: https://github.com/username/drug-recommender
   - PyPI: https://pypi.org/project/drug-recommender/
   - Docs: https://drug-recommender.readthedocs.io
   
   ## Installation
   ```bash
   pip install drug-recommender
   pip install drug-recommender[api]  # With API
   ```
   
   ## Deployment
   
   ### Docker
   ```bash
   docker-compose up -d
   ```
   
   ### Cloud (AWS/GCP/Azure)
   - See deployment/cloud_deploy.md
   
   ## Maintenance
   
   ### Updating Package
   1. Update version in pyproject.toml
   2. Update CHANGELOG.md
   3. Run tests: `pytest`
   4. Build: `python -m build`
   5. Publish: `twine upload dist/*`
   
   ### Monitoring
   - API logs: `docker logs <container>`
   - Health: `http://localhost:8000/api/v1/health`
   
   ## Support
   - Issues: GitHub Issues
   - Email: team@university.edu
   
   ## Future Enhancements
   - Machine learning-based collaborative filtering
   - Matrix factorization for predictions
   - Multi-language support
   - Real-time analysis dashboard
   - Integration with EHR systems
   ```

**Deliverable**:
- Production Docker deployment
- Demo script and materials
- Presentation
- Video tutorial (optional)
- Complete handover documentation

---

## **PyPI Package Features Summary**

### **Installation Options**:
```bash
# Basic installation
pip install drug-recommender

# With API support
pip install drug-recommender[api]

# With development tools
pip install drug-recommender[dev]

# With all extras
pip install drug-recommender[all]
```

### **Usage as Library**:
```python
from drug_recommender import DrugRecommender

# Quick recommendations
recommender = DrugRecommender(data_path="reviews.csv")
results = recommender.recommend("diabetes", strategy="recency")
```

### **Usage as API**:
```bash
# Start server
python -m drug_recommender.api

# Or with Docker
docker run -p 8000:8000 drug-recommender
```

### **Key Advantages of PyPI Package**:
1. ✅ **Easy Distribution**: `pip install` makes it accessible worldwide
2. ✅ **Version Management**: Semantic versioning and dependency management
3. ✅ **Dual Purpose**: Library + API in one package
4. ✅ **Professional**: Follows Python packaging best practices
5. ✅ **Open Source**: Community can contribute and extend
6. ✅ **Citable**: Researchers can cite and use in papers
7. ✅ **Portable**: Works on any platform with Python

---

## **Evaluation Criteria**

### **PyPI Package Quality (30%)**
- Package structure and organization
- Documentation quality (README, docstrings)
- Following Python packaging standards
- Proper dependency management
- Semantic versioning

### **Code Quality (25%)**
- Clean, pythonic code
- Type hints usage
- Comprehensive docstrings
- Error handling
- Design patterns

### **API Implementation (20%)**
- RESTful design
- Proper HTTP methods
- Error responses
- Documentation (OpenAPI)
- Performance

### **Testing (15%)**
- Unit test coverage (>85%)
- Integration tests
- API tests
- Performance tests

### **Documentation (10%)**
- README quality
- Usage examples
- API documentation
- Installation guide
- Contributing guide

---

## **Success Metrics**

By end of Week 4:

✅ **PyPI Package Published** and installable via pip  
✅ **Documentation** complete and deployed online  
✅ **Test Coverage** >85%  
✅ **API Functional** with all core endpoints  
✅ **Docker Deployment** production-ready  
✅ **Examples** comprehensive and working  
✅ **Demo** presentation-ready  
✅ **GitHub** properly configured with CI/CD  

---

## **Weekly Milestones**

### **Week 1**: Foundation ✅
- Domain understanding documented
- Package structure created
- Architecture designed
- Development environment ready

### **Week 2**: Core Library ✅
- All core modules implemented
- Unit tests written (>70% coverage)
- Docstrings complete
- Basic examples working

### **Week 3**: API & Preparation ✅
- FastAPI implementation complete
- Package documentation written
- README and examples finalized
- Pre-publication checks passed

### **Week 4**: Publication & Demo ✅
- Published to PyPI
- API deployed with Docker
- Documentation online
- Demo materials ready
- Final presentation delivered

---

## **Additional Resources**

### **Python Packaging**:
- [Python Packaging User Guide](https://packaging.python.org/)
- [PyPI Publishing Guide](https://packaging.python.org/tutorials/packaging-projects/)
- [Semantic Versioning](https://semver.org/)

### **Recommendation Systems**:
- [Collaborative Filtering Basics](https://en.wikipedia.org/wiki/Collaborative_filtering)
- [Surprise Library Documentation](http://surpriselib.com/)
- [Scikit-learn Metrics](https://scikit-learn.org/stable/modules/metrics.html)

### **FastAPI**:
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pydantic Models](https://docs.pydantic.dev/)

### **Testing**:
- [pytest Documentation](https://docs.pytest.org/)
- [Coverage.py](https://coverage.readthedocs.io/)

### **Documentation**:
- [Sphinx Documentation](https://www.sphinx-doc.org/)
- [Read the Docs](https://readthedocs.org/)

---

## **Conclusion**

This revised agenda transforms the project into a **professional PyPI package** that:

1. **Serves the Python community** through easy `pip install`
2. **Provides both library and API** functionality
3. **Follows industry best practices** for Python packaging
4. **Is production-ready** with Docker deployment
5. **Is well-documented** with examples and tutorials
6. **Can be extended** by the open-source community

Students will gain valuable experience in:
- Professional Python package development
- PyPI publishing workflow
- Recommendation system implementation
- API development with FastAPI
- Docker containerization
- Technical documentation
- Open-source project management

The package will be a portfolio piece demonstrating real-world software engineering skills applicable to health tech, data science, and software development careers.