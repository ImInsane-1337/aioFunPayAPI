# aioFunPayAPI

Асинхронная библиотека для легкого написания ботов FunPay. Полностью базируется на `asyncio` и `aiohttp`.

## Установка

Для установки библиотеки из локального каталога:
```bash
pip install .
```

## Быстрый старт

Пример простого асинхронного бота, который отвечает на сообщение с текстом «привет»:

```python
import asyncio
from FunPayAPI import Account, Runner
from FunPayAPI.enums import EventTypes

async def main():
    # Создаем класс аккаунта и асинхронно получаем его данные.
    acc = await Account(golden_key="YOUR_GOLDEN_KEY").get()
    print(f"Авторизован как {acc.username} (ID: {acc.id})")

    # Создаем прослушиватель событий.
    runner = Runner(acc)

    # Асинхронно прослушиваем события
    async for event in runner.listen(requests_delay=6.0):
        # Если событие — новое сообщение
        if event.type == EventTypes.NEW_MESSAGE:
            # Если текст сообщения "привет" и оно отправлено не нами
            if event.message.text and event.message.text.lower() == "привет" and event.message.author_id != acc.id:
                # Отправляем ответное сообщение асинхронно
                await acc.send_message(event.message.chat_id, "Ну привет...")
                runner.mark_as_by_bot(event.message.chat_id, event.message.id)

if __name__ == "__main__":
    asyncio.run(main())
```

## Выдача товара при новом заказе

Пример асинхронного бота, который выдает товар при новом оплаченном заказе:

```python
import asyncio
from FunPayAPI import Account, Runner
from FunPayAPI.enums import EventTypes, OrderStatuses

async def main():
    acc = await Account(golden_key="YOUR_GOLDEN_KEY").get()
    runner = Runner(acc)

    async for event in runner.listen(requests_delay=6.0):
        # Если событие — новый заказ
        if event.type == EventTypes.NEW_ORDER:
            # Обязательно очищаем ID от знака '#'
            clean_id = event.order.id.replace("#", "")
            
            if event.order.status == OrderStatuses.PAID:
                order_info = await acc.get_order(clean_id)
                # Отправляем товар в чат покупателю
                await acc.send_message(
                    order_info.chat_id,
                    f"Привет, {event.order.buyer_username}!\nВот твой товар: ..."
                )

if __name__ == "__main__":
    asyncio.run(main())
```
