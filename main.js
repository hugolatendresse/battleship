
function create_field() {
    var field = []
    for(var i = 0; i<10; i++) {
        field.push(new Array(10).fill(0))
    }
    return field
}

field1 = create_field()
field2 = create_field()



console.log(field1)