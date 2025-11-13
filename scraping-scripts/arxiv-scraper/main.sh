#!/bin/bash
# Main workflow script for arXiv literature review
# Runs the complete pipeline: scrape -> filter -> dedupe -> curate -> generate

set -e  # Exit on error

echo "=================================================="
echo "  arXiv Literature Review Pipeline"
echo "=================================================="
echo ""

# Check if API key is set in .env file
if [ ! -f "../.env" ]; then
    echo "❌ ERROR: .env file not found in project root"
    echo ""
    echo "Please create a .env file with:"
    echo "  KEY=your-api-key-here"
    echo ""
    exit 1
fi

# Step 1: Scrape arXiv
echo "📚 Step 1: Scraping arXiv for papers..."
echo "--------------------------------------------------"
python 1-scrape.py "$@"
echo ""
echo "✅ Step 1 complete!"
echo ""

# Step 2: Filter results by relevance
echo "🤖 Step 2: Filtering papers by relevance with LLM..."
echo "--------------------------------------------------"
python 2-filter_results.py
echo ""
echo "✅ Step 2 complete!"
echo ""

# Step 3: Extract links from DOCX (if needed)
if [ ! -f "results/shallow-review-2025-links.csv" ]; then
    echo "📄 Step 3: Extracting links from DOCX..."
    echo "--------------------------------------------------"
    python 3-docx_links_to_csv.py
    echo ""
    echo "✅ Step 3 complete!"
    echo ""
else
    echo "⏭️  Step 3: Skipping DOCX link extraction (already exists)"
    echo ""
fi

# Step 4: Find unique papers (not in existing review or Lenz papers)
echo "🔍 Step 4: Finding unique papers..."
echo "--------------------------------------------------"
python 4-find-unique-arxiv-links.py
echo ""
echo "✅ Step 4 complete!"
echo ""

# Step 5: Curate papers against post content
echo "✨ Step 5: Curating papers against review content..."
echo "--------------------------------------------------"
python 5-curate-unique-arxiv-links.py
echo ""
echo "✅ Step 5 complete!"
echo ""

# Step 6: Generate taxonomy and editorial
echo "📝 Step 6: Generating taxonomy and editorial..."
echo "--------------------------------------------------"
python 6-create-taxonomy-and-editorial-from-curated-links.py
echo ""
echo "✅ Step 6 complete!"
echo ""

# Summary
echo "=================================================="
echo "  ✨ Pipeline Complete!"
echo "=================================================="
echo ""
echo "Key output files:"
echo "  1. results/1-arxiv_raw_search_results.csv - All scraped papers"
echo "  2. results/2-arxiv_highly_relevant_results.csv - Highly relevant papers"
echo "  3. results/4-arxiv_new_links_only.csv - New papers (not in review)"
echo "  4. results/5-arxiv_curated_relevant_only.csv - Curated papers for inclusion"
echo "  5. results/6-taxonomy-and-editorial.txt - Final taxonomy & editorial"
echo ""
echo "📖 Review the final output at:"
echo "  results/6-taxonomy-and-editorial.txt"
echo ""

