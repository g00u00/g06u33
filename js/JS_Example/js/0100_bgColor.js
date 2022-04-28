function random(number) {
  return Math.floor(Math.random()*(number+1))//генерируем случайное число для заданного диапазона
}
function body_bgColor() {
  var btn = document.querySelector('button')//определяем нужный узел
  var rndCol = 'rgb(' + random(255) + ',' + random(255) + ',' + random(255) + ')'//задаем цвет
  console.log(rndCol)
  document.body.style.backgroundColor = rndCol //меняем цвет
  btn.innerHTML = "Цвет изменен на:  " + rndCol //меняем свойство узла
}