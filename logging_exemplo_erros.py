from loguru import logger

logger.debug("Um aviso para o desenvolvedor")
# somente aparece ao debugar

logger.info("Informação importante do processo")

logger.warning("Um aviso que algo vai parar de funcionar")

logger.error("Aconteceu um falha")

logger.critical("Aconteceu uma falha que aborta a aplicaçao")

"""
Ao executar esse py, aparecera as mensagens criadas

2025-10-02 18:34:42.960 | DEBUG    | __main__:<module>:3 - Um aviso para o desenvolvedor
2025-10-02 18:34:42.960 | INFO     | __main__:<module>:6 - Informação importante do processo
2025-10-02 18:34:42.960 | WARNING  | __main__:<module>:8 - Um aviso que algo vai parar de funcionar
2025-10-02 18:34:42.960 | ERROR    | __main__:<module>:10 - Aconteceu um falha
2025-10-02 18:34:42.960 | CRITICAL | __main__:<module>:12 - Aconteceu uma falha que aborta a aplicaçao

"""