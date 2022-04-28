function CheckFields(form){
    var elems = form.elements
    var result_p = document.getElementById('result')

    console.log("elems", elems)
    console.log("elems[0] ", elems[0])
    console.log("elems[0].value ", elems[0].value)
    console.log("elems.a.value ", elems.a.value)
    console.log("typeof(elems.a.value) ", typeof(elems.a.value))
    console.log("result_p: ", result_p)
    console.log("typeof(result_p): ", typeof(result_p))

    if (parseFloat(elems.x.value) >= parseFloat(elems.a.value) && parseFloat(elems.x.value) <= parseFloat(elems.b.value)){
        result_p.innerHTML = "x принадлежит заданному промежутку";
        var check = true;
        }
        else{
            result_p.innerHTML = "x не принадлежит заданному промежутку";
            var check = false;
        }

    if (check) {
        document.getElementById("UserEnter").submit();
8       }
        else{
            alert ( "Есть недостатки, повторите ввод" )
        }
    console.log("result_p: ", result_p)
}
        