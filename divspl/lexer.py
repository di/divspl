from rply import LexerGenerator

lg = LexerGenerator()

lg.add("ELLIPSIS", r"\.\.\.")
lg.add("NUMBER", r"\d+")
lg.add("EQUALS", r"=")
lg.add("WORD", r"[a-z]+")

lg.ignore(r"\s+")  # Ignore whitespace
lg.ignore(r"#.*\n")  # Ignore comments

lexer = lg.build()
