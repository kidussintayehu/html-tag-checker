def checkMaching(open,close):
    # this funtion check if the openig tag at specific indexs 
    # in the list are matche to the closing tag
    open_tag = ["<html>","<!DOCTYPE>","<head>","<title>"
    ,"<div>","<body>", "<span>","<a>", "<p>"
    ,"<table>","<thead>","<tbody>","<tr>","<td>"
    ,"<br>","<script>","<img>","<ul>","<hr>","<strong>"]
    closes_tag = ["</html>","<!DOCTYPE>","</head>","</title>"
    ,"</div>","</body>","</span>","</a>", "</p>"
    ,"</table>","</thead>","</tbody>","<tr>","</td>",
    "</br>","</script>","</img>","</ul>","</hr>","</strong>"]
    return open_tag.index(open) == closes_tag.index(close)



mylist=[]
checker = True
tag= open('kid.html','r')    # open file in the same directory as the programe file
splited = tag.read().split()  # read the file and split if finds a space
for i in splited:
    #
    # this if condition check the opening tags and
    # exaptions like "DOCTYPE"
    if i[0] == "<" and i[1] != "/":
        if not i.endswith('>'):
            mylist.insert(0, i+'>')
        else:
            mylist.insert(0,i) 
    # this condition check the closing tags and
    #  using checkMaching checks if it matchs with the opening tag
    elif i[0] == "<" and i[1] == "/":
        if len(mylist)==0:
            checker = False
        else:
            top = mylist.pop()
            if checkMaching(top,i):
                checker = True
    else:
        pass
if checker and len(mylist)==0:
    print("your tag is correct")
else:
    print("your tag is incorrectly typed")

    


