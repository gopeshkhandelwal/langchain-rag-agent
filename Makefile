# === Configuration ===
PYTHON := python3
APP_DIR := agent_app
ENTRY := $(APP_DIR)/main.py
ENV_FILE := .env

# === Commands ===

install:
	@echo "🔧 Installing dependencies..."
	pip install -r requirements.txt

run:
	@echo "🚀 Running agent..."
	PYTHONPATH=. python3 $(ENTRY)

lint:
	@echo "🧹 Running linter..."
	flake8 $(APP_DIR)

format:
	@echo "🎨 Formatting code..."
	black $(APP_DIR)

clean:
	@echo "🧼 Cleaning pyc files..."
	find . -name "*.pyc" -delete

help:
	@echo "📘 Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' Makefile | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-12s\033[0m %s\n", $$1, $$2}'

# === Descriptions ===

install:       ## Install Python dependencies
run:           ## Run the LangChain agent
lint:          ## Run flake8 linter
format:        ## Format code with black
clean:         ## Remove Python cache files
help:          ## Show this help menu
