page = {"title": "Тег BODY",
        "charset": "utf-8",
        "alert": "Документ загружен",
        "p": "Ut wisis enim ad minim veniam,  suscipit lobortis nisl ut aliquip ex ea commodo consequat."}

template = """ 
<!DOCTYPE HTML>
<html>
 <head>
  <title> ? </title>
  <meta charset=?>
 </head>
 <body onload="alert(?)">

  <p>?</p>

 </body>
</html>
"""

# for key, value in page.items():
#         if key in template:
#                 print(key)
new_template = []
for line in template.splitlines():
        for key, value in page.items():
                if key in line:
                        line = line.replace('?', value, 1)
                        break
        new_template.append(line)
print("\n".join(new_template))
