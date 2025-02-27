from docling.document_converter import DocumentConverter
from utils.sitemap import get_sitemap_urls

converter = DocumentConverter()

Link = "isert the link to the desired PDF here"
# --------------------------------------------------------------
# Basic PDF extraction
# --------------------------------------------------------------

result = converter.convert(Link)

document = result.document
markdown_output = document.export_to_markdown()
json_output = document.export_to_dict()

print(markdown_output)

# --------------------------------------------------------------
# Basic HTML extraction
# --------------------------------------------------------------



result = converter.convert(Link)

document = result.document
markdown_output = document.export_to_markdown()
print(markdown_output)

# --------------------------------------------------------------
# Scrape multiple pages using the sitemap
# --------------------------------------------------------------

sitemap_urls = get_sitemap_urls(Link)
conv_results_iter = converter.convert_all(sitemap_urls)

docs = []
for result in conv_results_iter:
    if result.document:
        document = result.document
        docs.append(document)
