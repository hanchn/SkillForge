.PHONY: dev stop restart

PORT ?= 8080

dev:
	@echo "Starting SkillForge Dashboard on http://localhost:$(PORT)"
	@python3 -m http.server $(PORT)

stop:
	@echo "Stopping SkillForge server..."
	@pkill -f "python3 -m http.server" || echo "No server running."

restart: stop dev
