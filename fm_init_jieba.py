
from typing import Callable
from jieba import lcut as jieba_lcut, setLogLevel as jieba_set_log_level

jieba_set_log_level('WARNING')

def jieba_tokenizer_provided_via_user_files_init(txt: str) -> list[str]:

    return list(token for token in jieba_lcut(txt) if token is not None)

def jieba_tokenizers_provider() -> list[tuple[str, Callable]]:

    return [("zh", jieba_tokenizer_provided_via_user_files_init)]
