#!/bin/bash

# Startup script for WordCloud App

echo "🚀 Starting WordCloud App Setup..."

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo -e "${RED}❌ Docker is not installed. Please install Docker first.${NC}"
    exit 1
fi

echo -e "${GREEN}✅ Docker found${NC}"

# Check if Docker Compose is installed
if ! command -v docker-compose &> /dev/null; then
    echo -e "${RED}❌ Docker Compose is not installed. Please install Docker Compose first.${NC}"
    exit 1
fi

echo -e "${GREEN}✅ Docker Compose found${NC}"

# Build and start the application
echo -e "${BLUE}📦 Building Docker image...${NC}"
docker-compose build

echo -e "${BLUE}🚀 Starting application...${NC}"
docker-compose up -d

echo -e "${GREEN}✅ Application started successfully!${NC}"
echo -e "${BLUE}🌐 Access the app at: http://localhost:8501${NC}"
echo -e "${BLUE}📊 View logs: docker-compose logs -f${NC}"
echo -e "${BLUE}🛑 Stop app: docker-compose down${NC}"
