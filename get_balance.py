import asyncio
from aioFunPayAPI import Account
from aioFunPayAPI.common import exceptions

async def get_my_balance():
    # Запрашиваем golden_key у пользователя
    golden_key = input("Введите ваш golden_key от FunPay: ").strip()
    if not golden_key:
        print("Ошибка: golden_key не может быть пустым.")
        return

    print("\n[1/3] Подключение к FunPay и авторизация...")
    try:
        # Инициализация аккаунта
        account = await Account(golden_key=golden_key).get()
        print(f"Успешно авторизован как: {account.username} (ID: {account.id})")
        
        print("[2/3] Запрос баланса...")
        # Получение баланса
        balance = await account.get_balance()
        
        print("\n[3/3] Результаты:")
        print("=" * 45)
        print(f"{'Валюта':<10} | {'Общий баланс':<15} | {'Доступно к выводу':<15}")
        print("=" * 45)
        print(f"{'RUB (₽)':<10} | {balance.total_rub:<15.2f} | {balance.available_rub:<15.2f}")
        print(f"{'USD ($)':<10} | {balance.total_usd:<15.2f} | {balance.available_usd:<15.2f}")
        print(f"{'EUR (€)':<10} | {balance.total_eur:<15.2f} | {balance.available_eur:<15.2f}")
        print("=" * 45)
        
    except exceptions.UnauthorizedError:
        print("\nОшибка: Не удалось авторизоваться. Проверьте правильность введённого golden_key.")
    except exceptions.RequestFailedError as e:
        print(f"\nОшибка запроса к FunPay API: {e.short_str()}")
    except Exception as e:
        print(f"\nПроизошла непредвиденная ошибка: {e}")

if __name__ == "__main__":
    try:
        asyncio.run(get_my_balance())
    except KeyboardInterrupt:
        print("\nПрограмма принудительно остановлена.")
