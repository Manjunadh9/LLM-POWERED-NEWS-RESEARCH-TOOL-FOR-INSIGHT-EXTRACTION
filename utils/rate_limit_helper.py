#!/usr/bin/env python3
"""
Gemini API Rate Limit Helper
Check your current API usage and rate limits
"""

import os
import time
from dotenv import load_dotenv

load_dotenv()

def check_rate_limits():
    """Display rate limit information for Gemini API"""
    
    print("📊 Gemini API Rate Limits & Usage Tips")
    print("=" * 50)
    
    print("\n🚀 **Free Tier Limits:**")
    print("• Requests per minute: 15")
    print("• Requests per day: 1,500")
    print("• Input tokens per minute: 50,000")
    print("• Input tokens per day: 15,000,000")
    
    print("\n💡 **Cost-Effective Models:**")
    print("• gemini-1.5-flash: Fastest, most cost-effective")
    print("• gemini-1.5-pro: Higher quality, more expensive")
    print("• gemini-1.0-pro: Good balance, stable")
    
    print("\n🔧 **Optimization Tips:**")
    print("• Use smaller text chunks (200 tokens vs 300)")
    print("• Reduce max_tokens in responses")
    print("• Wait 1 minute between batches of requests")
    print("• Process URLs in smaller batches")
    
    print("\n📈 **Upgrade Options:**")
    print("• Pay-as-you-go: $0.0005 per 1K input tokens")
    print("• Higher rate limits with paid plans")
    print("• Visit: https://makersuite.google.com/app/apikey")
    
    print("\n⏰ **Current Time:**", time.strftime("%Y-%m-%d %H:%M:%S"))
    print("💡 **Tip:** Rate limits reset every minute")

if __name__ == "__main__":
    check_rate_limits()
