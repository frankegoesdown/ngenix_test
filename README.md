# ngenix_test
ngenix test task


0. Create zip archives with 50 xml files in temp folder:
        python generate.py

0. Create csv files with parsed data from zip archives in temp folder:
        python parse.py

0. Remove all folders with files:
        python.clean

0. Run all commands:
        python main.py

Requirements:
        pip install -r requirements.txt

================

DESCRIPTION

================

Написать программу на Python, которая делает следующие действия:

0. Создает 50 zip-архивов, в каждом 100 xml файлов со случайными данными следующей структуры:


        <root>
            <var name='id' value='<случайное уникальное строковое значение>'/>
            <var name='level' value='<случайное число от 1 до 100>'/>
            <objects>
                <object name='<случайное строковое значение>'/>
                <object name='<случайное строковое значение>'/>
            </objects>
        </root>


        В тэге objects случайное число (от 1 до 10) вложенных тэгов object.

0. Обрабатывает директорию с полученными zip архивами, разбирает вложенные xml файлы и формирует 2 csv файла:

        Первый: id, level - по одной строке на каждый xml файл

        Второй: id, object_name - по отдельной строке для каждого тэга object (получится от 1 до 10 строк на каждый xml файл)

        Очень желательно сделать так, чтобы задание 2 эффективно использовало ресурсы многоядерного процессора. 

        Также желательно чтобы программа работала быстро.

 ================
