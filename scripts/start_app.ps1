# Article Research Tool Startup Script
# This script starts the Streamlit application with the correct environment

Write-Host "🚀 Starting Article Research Tool..." -ForegroundColor Green

# Check if .env file exists
if (-Not (Test-Path ".env")) {
    Write-Host "❌ Missing .env file" -ForegroundColor Red
    Write-Host "Please create a .env file with your GEMINI_API_KEY" -ForegroundColor Yellow
    Write-Host "Example: GEMINI_API_KEY=your_actual_api_key_here" -ForegroundColor Yellow
    exit 1
}

Write-Host "✅ Environment file found" -ForegroundColor Green
Write-Host "📊 Rate limiting enabled for free tier" -ForegroundColor Cyan

# Check if port 8501 is available
$portCheck = netstat -an | findstr :8501
if ($portCheck) {
    Write-Host "⚠️  Port 8501 is in use. Stopping existing processes..." -ForegroundColor Yellow
    Stop-Process -Name "python" -Force -ErrorAction SilentlyContinue
    Stop-Process -Name "python3.13" -Force -ErrorAction SilentlyContinue
    Stop-Process -Name "streamlit" -Force -ErrorAction SilentlyContinue
    Start-Sleep -Seconds 3
}

# Start the Streamlit application
Write-Host "🔄 Starting Streamlit app..." -ForegroundColor Cyan
Write-Host "📱 App will be available at: http://localhost:8501" -ForegroundColor Cyan
Write-Host "🔄 Press Ctrl+C to stop the application" -ForegroundColor Yellow
Write-Host "💡 Rate limiting: 15 requests/minute (free tier)" -ForegroundColor Yellow

.\venv\Scripts\streamlit.exe run main.py --server.port 8501
