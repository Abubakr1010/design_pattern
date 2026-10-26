from abc import ABC, abstractmethod

class Document(ABC):

    @abstractmethod
    def export(self, data:str) -> str:
        pass


class PDFDocument(Document):

    def export(self, data:str) -> str:
        return f"[PDF Format] Exporting data: '{data}' as a rigid, styled PDF file."


class WordDocument(Document):

    def export(self, data:str) -> str:
        return f"[Word Format] Exporting data: '{data}' as a rigid, styled PDF file."


class DocumentExporter(ABC):

    @abstractmethod
    def create_document(self):
        pass


    def export_data(self, data:str) -> str:
        doc = self.create_document()
        result = doc.export(data)
        return result

class PDFExporter(DocumentExporter):

    def create_document(self) -> Document:
        return PDFDocument()
        

class WordExporter(DocumentExporter):

    def create_document(self) -> Document:
        return WordDocument()


if __name__ == "__main__":

    pdf_factory = PDFExporter()
    print (pdf_factory.export_data("Q3 Financial report"))

    word_factory = WordExporter()
    print (word_factory.export_data("Q3 Financial report"))
    
        


        

      
