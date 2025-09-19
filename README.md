# Todo List CLI Ilovasi

Python bilan yozilgan oddiy buyruq satri (CLI) todo list ilovasi. Vazifalaringizni oddiy buyruqlar orqali boshqarishingiz va ularni `todos.json` faylida saqlashingiz mumkin.

## Xususiyatlar

- **Vazifalarni qo'shish**.
- **Barcha vazifalarni ro'yxatini ko'rish**.
- **Vazifalarni bajarilgan deb belgilash** yoki **o'chirish**.
- **Buyruq satri interfeysi** bilan qulay ishlash.

## O'rnatish

1. Repozitoriyani klonlash:
   ```bash
   git clone https://github.com/yourusername/todo-cli.git
   cd todo-cli
````

2. Python 3.x o'rnatilganligini tekshiring.

## Foydalanish

Ilovani ishga tushirish uchun:

```bash
python todo.py
```

Quyidagi buyruqlar mavjud:

* **`add <task>`**: Yangi vazifa qo'shish.
* **`list`**: Barcha vazifalarni ro'yxatini ko'rsatish.
* **`done <n>`**: `<n>` raqamli vazifani bajarilgan deb belgilash.
* **`del <n>`**: `<n>` raqamli vazifani o'chirish.
* **`exit`**: Ilovadan chiqish.

## Fayl Tuzilishi

* `todo.py`: Asosiy dastur fayli.
* `todos.json`: Vazifalar saqlanadigan JSON fayli.

## Litsenziya

MIT Litsenziyasi. Batafsil ma'lumot uchun [LICENSE](LICENSE) faylini ko'rib chiqing.