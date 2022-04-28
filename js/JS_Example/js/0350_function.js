var doAnalizeMy, doAnalizeNew, doCalculate, doSubmit 
var myVariable, newVariable 
var myVariableCalc, newVariableCalc, MyVariablesCalcSum = 0,  myVariablesCalc = []
var result_p = document.getElementById('result')

doAnalizeMy = function(myVariable){
    var result_p = document.getElementById('myResult')
    console.log("doAnalizeMy myVariable:", myVariable)
    myVariableCalc = myVariable
    result_p.innerHTML = " myVariableCalc: " +  myVariableCalc;
    return(myVariable)
}    

doAnalizeNew = function(newVariable){
    var result_p = document.getElementById('newResult')
    console.log("doAnalizeNew_newVariable: ",newVariable)
    newVariableCalc = newVariable
    result_p.innerHTML = " newVariableCalc: " +  newVariableCalc;
    return(newVariable)
}

doCalculate = function(){
    myVariablesCalc.push(parseInt(myVariableCalc))
    MyVariablesCalcSum  += parseInt(myVariableCalc)
    console.log ("doCalculate_:" + "\nmyVariableCalc: " +  myVariableCalc  + "   myVariablesCalc: "+ myVariablesCalc + ";   MyVariablesCalcSum:" + MyVariablesCalcSum + "; \nnewVariableCalc: "+ newVariableCalc)
    alert ("doCalculate_:"  + "\nmyVariableCalc: " +  myVariableCalc + "myVariablesCalc: "+ myVariablesCalc + ";  MyVariablesCalcSum:" + MyVariablesCalcSum  +  ";\n\nnewVariableCalc: "+ newVariableCalc )
}
   
doSubmit = function(){
   let form = document.createElement('form');
   form.action = 'http://bim.nn2000.info/cgi-bin/f_submission.pl';
   form.method = 'get';
   form.target = 'blank'
   form.innerHTML = '<input type="Hidden" name="MyVariablesCalcSum" value=' + MyVariablesCalcSum +'>';
   form.innerHTML += '<input type="Hidden" name="myVariablesCalc" value=' + myVariablesCalc +'>';
   form.innerHTML +=  '<input type="Hidden" name="file_name" value="file.txt" ><input type="Hidden"  name="tmp1" value="1">'
   document.body.append(form);
   form.submit();
}
