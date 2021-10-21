const todos = []

window.onload = () => {
    const form = document.getElementById('todo')
    form.onsubmit = (e) => {
        e.preventDefault();
        const todo = document.getElementById('caja')
        const todoText = todo.value;
        todo.value = ''
        todos.push(todoText)
        const todoList = document.getElementById('list')
        todoList.innerHTML = ''
        for (let i=todos.length;i>0;i--) {
            todoList.innerHTML += '<li class="item" id=' + 'item' + i.toString() +'>' + todos[i-1] + '<a class="trash"><i class="fas fa-trash-alt"></i></a>' +'</li>'
        
            console.log('item' + i.toString())
        }


        console.log(todos)
        let id = "item" + (todos.length)
        let scale0 = "scale(0)"
        let scale1 = "scale(1)"
        console.log(id)

        document.getElementById(id).style.transform = scale0
        
       
        setTimeout(()=>{
            document.getElementById(id).style.transform =scale1
        },001)
    }
}