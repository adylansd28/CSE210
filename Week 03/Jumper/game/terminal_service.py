class TerminalService:
     
    def read_text(self, prompt):
        return input(prompt)
        
    def write_text(self, text):
        print(text)