from loguru import logger

logger.add(
    "logs/meu_arquivo_de_logs.log",
    format = "{time} | <{level}> | {message} | <{file}>",
    level = "INFO"
    )
# AO INFORMAR O <level>, ELE IRA SALVAR A PARTIR NIVEL DELE
# INFO > WARNING > CRITICAL > ERROR

# EM TELA SERA PRINTADO TODOS OS logger ONDE O PYTHON ENTRE

def soma(x, y):
    try:
        soma = x + y
        logger.info(f"Voce digitou valores corretos, parabens! Resultado: {soma}")
        logger.warning(f"Cuidado para nao digitar numero erroa!")
        return soma
    except:
        logger.critical("Avisei para nao digitar numero errado.")
        logger.error("Voce tem que digitar valores corretos.")

soma(2,3)
soma(2,"3")