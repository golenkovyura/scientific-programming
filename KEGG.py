def parse_gene_paths(table_text: str) -> dict:
    """Предобработка текстового файла в словарь"""
    gene_in_path = {}
    for word in table_text.split():
        if word.startswith('hsa'):
            gene_in_path[word] = [] # Ключ - строка, начинающаяся с 'hsa'
        else:
            gene_in_path[list(gene_in_path.keys())[-1]].append(word) # В последний ключ добавляем все гены
    return gene_in_path


def count_paths_for_gene(
    gene_in_path: dict,
    gene: str,
    path_part: str
) -> int:
    """Подсчет подходящих путей"""
    c = 0
    for key, value in gene_in_path.items():
        if path_part in key.split('_') and gene in value[1:]:
            c += 1
    return c
