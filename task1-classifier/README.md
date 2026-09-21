# Task 1 — Message Classifier

## Run

```bash
python task1-classifier/classify.py
```

No dependencies. Python 3.8+ only.

---

## Result

```
[1] Как получить справку о месте учёбы?
    Категория : справка
    Ответ     : Для получения справки о месте учёбы обратитесь в учебный отдел в часы приёма. Заявление можно подать лично или через личный кабинет студента.

[2] В столовой очередь, еда холодная.
    Категория : жалоба
    Ответ     : Приносим извинения за неудобства. Ваше обращение передано администрации столовой для принятия мер.

[3] Хочу записаться на консультацию завтра.
    Категория : другое
    Ответ     : Для записи на консультацию, пожалуйста, уточните удобное время и укажите, к какому специалисту вы хотели бы обратиться.

[4] Пропал Wi‑Fi в корпусе B.
    Категория : жалоба
    Ответ     : Приносим извинения за неудобства, связанные с отсутствием Wi-Fi. Заявка передана в технический отдел — специалисты уже занимаются устранением неполадки.

[5] Где парковка для гостей?
    Категория : другое
    Ответ     : Информацию о парковке для гостей вы можете получить на стойке охраны при входе или у дежурного администратора.
```

---

## Limitations

- **Rule-based only.** The keyword list is short; unusual phrasing may be misclassified.
- **LLM swap.** The `classify()` function has a clear single-string input / single-string output contract, so it can be replaced by one `openai.chat.completions.create()` call with a system prompt listing the three categories — no other code needs to change.
