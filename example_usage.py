from client import MultimodalDocumentLayoutAstParserClient

def main():
    client = MultimodalDocumentLayoutAstParserClient()
    res = client.parse_document_to_unified_ast('https://assets.genpark.ai/docs/scientific_paper.pdf')
    print('Docling AST Parser: ' + res['parsing_job_id'] + ' (' + str(res['pages_parsed_count']) + ' pages)')
    print('Tables: ' + str(res['complex_tables_structured_count']) + ' | LaTeX Equations: ' + str(res['latex_equations_extracted_count']))
    print('Reading Order Accuracy: ' + str(res['reading_order_recovery_accuracy_pct']) + '%')
    print('Export URL: ' + res['unified_markdown_export_url'])

if __name__ == '__main__':
    main()
