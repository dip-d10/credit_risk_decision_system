import os
from pathlib import Path

# Project name (root folder)
project_name = "credit-intelligence-system"

# ================================
# 📁 Folder + File Structure
# ================================
list_of_files = [

    # Root files
    ".gitignore",
    "requirements.txt",
    "Dockerfile",
    "README.md",
    "main.py",

    # ================= APP =================
    "app/__init__.py",
    "app/main.py",

    "app/api/__init__.py",
    "app/api/routes/__init__.py",
    "app/api/routes/predict.py",
    "app/api/routes/explain.py",
    "app/api/routes/simulate.py",
    "app/api/routes/chat.py",

    "app/schemas/__init__.py",
    "app/schemas/input_schema.py",
    "app/schemas/output_schema.py",

    "app/services/__init__.py",
    "app/services/prediction_service.py",
    "app/services/explanation_service.py",
    "app/services/simulation_service.py",

    # ================= INGESTION =================
    "ingestion/__init__.py",
    "ingestion/user_input.py",
    "ingestion/bureau_data.py",
    "ingestion/macro_scraper.py",
    "ingestion/news_scraper.py",
    "ingestion/pipeline.py",

    # ================= FEATURES =================
    "features/__init__.py",
    "features/preprocess.py",
    "features/feature_builder.py",
    "features/macro_features.py",
    "features/behavioral_features.py",
    "features/pipeline.py",

    # ================= MODELS =================
    "models/__init__.py",
    "models/utils.py",

    "models/pd_model/__init__.py",
    "models/pd_model/train.py",
    "models/pd_model/predict.py",

    "models/lgd_model/__init__.py",
    "models/lgd_model/train.py",
    "models/lgd_model/predict.py",

    "models/ead_model/__init__.py",
    "models/ead_model/train.py",
    "models/ead_model/predict.py",

    # ================= LLM =================
    "llm/__init__.py",
    "llm/embeddings.py",
    "llm/transaction_nlp.py",
    "llm/sentiment_analysis.py",
    "llm/explanation_llm.py",
    "llm/rag_pipeline.py",
    "llm/prompts/__init__.py",
    "llm/prompts/templates.py",

    # ================= EXPLAINABILITY =================
    "explainability/__init__.py",
    "explainability/shap_explainer.py",
    "explainability/feature_importance.py",
    "explainability/report_generator.py",

    # ================= DECISION ENGINE =================
    "decision_engine/__init__.py",
    "decision_engine/rules.py",
    "decision_engine/pricing.py",
    "decision_engine/credit_limit.py",
    "decision_engine/engine.py",

    # ================= SIMULATION =================
    "simulation/__init__.py",
    "simulation/simulator.py",
    "simulation/strategies.py",
    "simulation/metrics.py",

    # ================= MONITORING =================
    "monitoring/__init__.py",
    "monitoring/drift_detection.py",
    "monitoring/performance.py",
    "monitoring/alerts.py",
    "monitoring/logs.py",

    # ================= PIPELINES =================
    "pipelines/__init__.py",
    "pipelines/training_pipeline.py",
    "pipelines/inference_pipeline.py",
    "pipelines/batch_pipeline.py",

    # ================= FRONTEND =================
    "frontend/streamlit_app.py",

    # ================= TESTS =================
    "tests/__init__.py",
    "tests/test_models.py",
    "tests/test_api.py",
    "tests/test_pipeline.py",
    "tests/test_simulation.py",

    # ================= DATA =================
    "data/.gitkeep"
]

# ================================
# 📦 File Creation Logic
# ================================
for filepath in list_of_files:
    filepath = Path(project_name) / Path(filepath)

    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    # Create file if not exists
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w", encoding="utf-8") as f:

            # Add minimal boilerplate
            if filename.endswith(".py"):
                f.write("# Auto-generated file\n\n")

    else:
        print(f"File already exists: {filepath}")


print("\n✅ Project structure created successfully!")