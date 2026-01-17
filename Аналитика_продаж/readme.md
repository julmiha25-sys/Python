⭕4.Кейс1 (файл sales_data.csv): ELT для csv-файла продаж

Класс "Extraction" реализует метод from_csv(file_path) для извлечения данных из CSV-файла. Метод from_csv() возвращает полученные данные в виде списка объектов продаж.

Класс "Sale" (продажа имеет атрибуты:id, date, amount, product. Здесь реализованы геттеры и сеттеры (get_id, get_date и тд) для доступа к атрибутам продажи.

Класс "Transformation" реализуйт методы для фильтрации данных о продажах по заданным критериям. filter_by_date принимает start_date и end_date и возвращает только те, продажи, которые попали в этот промежуток. filter_by_amount принимает min_amount и max_amount и возвращает только те продажи, которые по сумме покупки попали в этот промежуток. Методы возвращают отфильтрованные данные в виде списка объектов "Продажа".

Класс "Loading" реализует метод to_csv(sales_data, file_path) для сохранения обработанных (отфильтрованных) данных в формате CSV.

Класс "Analysis" реализует методы для подсчета общей суммы продаж (calculate_total_sales), вычисления средней суммы продажи (calculate_average_sales) с округлением.

Пример выполнения:

[Sale(id=1, date='2023-04-25', amount=35.21, product='Product 6'), Sale(id=2, date='2022-08-31', amount=359.19, product='Product 9'), Sale(id=3, date='2023-01-22', amount=117.53, product='Product 5'), Sale(id=4, date='2022-12-15', amount=366.68, product='Product 4'), Sale(id=5, date='2023-03-06', amount=628.65, product='Product 2')]

[Sale(id=2, date='2022-08-31', amount=359.19, product='Product 9'), Sale(id=6, date='2022-08-04', amount=843.69, product='Product 3'), Sale(id=7, date='2022-10-13', amount=190.38, product='Product 7'), Sale(id=13, date='2022-09-02', amount=590.5, product='Product 3'), Sale(id=14, date='2022-07-12', amount=51.17, product='Product 1')]

522581.97

522.58
