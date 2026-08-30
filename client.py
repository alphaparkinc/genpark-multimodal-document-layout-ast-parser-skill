class MultimodalDocumentLayoutAstParserClient:
    def parse_document_to_unified_ast(self, document_pdf_url='https://assets.genpark.ai/docs/financial_sec_10k.pdf', parse_tables_as_html=True):
        return {
            'parsing_job_id': 'doc_ast_7721',
            'pages_parsed_count': 32,
            'complex_tables_structured_count': 14,
            'latex_equations_extracted_count': 8,
            'reading_order_recovery_accuracy_pct': 99.85,
            'unified_markdown_export_url': 'https://parsed.genpark.ai/ast/7721.json'
        }
