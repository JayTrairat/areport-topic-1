
def main():
    with open('assets/cosine_values_only_value_number.txt', 'r', encoding='utf8') as sources:
        contents = sources.readlines()
        contents = [content.strip() for content in contents]
        contents.sort(reverse=True)
        with open('assets/generate_number_for_ttest.txt', 'w', encoding='utf8') as writer:
            writer.write('\n'.join(contents[:10]))

    with open('assets/cosine_values_only_value_text.txt', 'r', encoding='utf8') as sources:
        contents = sources.readlines()
        contents = [content.strip() for content in contents]
        contents.sort(reverse=True)
        with open('assets/generate_text_for_ttest.txt', 'w', encoding='utf8') as writer:
            writer.write('\n'.join(contents[:10]))

    with open('assets/cosine_values_only_value_datetime.txt', 'r', encoding='utf8') as sources:
        contents = sources.readlines()
        contents = [content.strip() for content in contents]
        contents.sort(reverse=True)
        with open('assets/generate_datetime_for_ttest.txt', 'w', encoding='utf8') as writer:
            writer.write('\n'.join(contents[:10]))

    # with open('files/original.txt', 'r', encoding='utf8') as sources:
    #     contents = sources.readlines()
    #     contents = [content.strip() for content in contents]
    #     contents.sort(reverse=True)
    #     with open('files/original_for_ttest.txt', 'w', encoding='utf8') as writer:
    #         writer.write('\n'.join(contents[:100]))

if __name__ == '__main__':
    main()
