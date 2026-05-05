"""
AI-powered sales summary generator.
Uses OpenAI GPT to produce a natural-language executive summary
of the regional sales data — integrated into the PDF report pipeline.

Falls back gracefully if OPENAI_API_KEY is not set (CI-safe).
"""

import os
import json


def generate_ai_summary(regional_data: "pd.DataFrame") -> str:
    """
    Generate a natural-language executive summary of the sales data.

    Args:
        regional_data: DataFrame with columns ['Region', 'Total Sales']

    Returns:
        A string containing the AI-generated analysis, or a fallback message.
    """
    api_key = os.environ.get("OPENAI_API_KEY", "")
    if not api_key:
        return _fallback_summary(regional_data)

    try:
        import openai
        client = openai.OpenAI(api_key=api_key)

        # Build a compact data payload for the prompt
        data_json = regional_data.to_dict(orient="records")
        total = regional_data["Total Sales"].sum()
        top_region = regional_data.loc[regional_data["Total Sales"].idxmax(), "Region"]
        bottom_region = regional_data.loc[regional_data["Total Sales"].idxmin(), "Region"]

        prompt = f"""You are a business analyst. Analyse the following regional sales data and write a concise executive summary (3-4 sentences). 
Highlight: top performer, underperformer, overall trend, and one actionable recommendation.

Data:
{json.dumps(data_json, indent=2)}

Total revenue across all regions: ${total:,.2f}
Top region: {top_region}
Lowest region: {bottom_region}

Write only the summary paragraph, no headers, no bullet points."""

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=200,
            temperature=0.4,
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        return _fallback_summary(regional_data)


def _fallback_summary(regional_data) -> str:
    """Rule-based summary when OpenAI is unavailable (e.g., CI environment)."""
    try:
        total = regional_data["Total Sales"].sum()
        top = regional_data.loc[regional_data["Total Sales"].idxmax()]
        bottom = regional_data.loc[regional_data["Total Sales"].idxmin()]
        avg = total / len(regional_data)

        return (
            f"Total revenue across {len(regional_data)} regions: ${total:,.2f}. "
            f"Top performer: {top['Region']} (${top['Total Sales']:,.2f}). "
            f"Lowest performer: {bottom['Region']} (${bottom['Total Sales']:,.2f}). "
            f"Regional average: ${avg:,.2f}."
        )
    except Exception:
        return "Sales data processed. See chart and table for details."
