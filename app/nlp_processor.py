import traceback
import spacy
import ginza


class Nlp_processor():
    nlp = spacy.load('ja_ginza')

    #形態素解析
    async def morphological_analyzer(self, text:str):
        doc = self.nlp(text)

        try:
            if doc:
                token_lists=[]
                for sent in doc.sents:
                    for token in sent:
                        #  info = [
                        #     token.i,         # トークン番号
                        #     token.text,     # テキスト
                        #     token.lemma_,    # 基本形
                        #     token.pos_,      # 品詞
                        #     token.tag_,      # 品詞詳細
                        # ]
                        token_lists.append(token.text)
                        print(token_lists)

            return token_lists[0]

        except Exception as excep:
            print("Exception\n" + traceback.format_exc())

            return None