with open("article.html", 'r') as file:
    main = file.read()

main = main.replace('png', 'png?raw=true')

with open("article.html", 'w') as file:
    file.write(main)
