
function create_field() {
    var field = []
    for(var i = 0; i<10; i++) {
        field.push(new Array(10).fill(0))
    }
    return field
}

function create_boats() {
    return [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
}

field1 = create_field()
field2 = create_field()

boats1 = create_boats()
boats2 = create_boats()


field1[0][0] = 1
field2[1][1] = 1

function add_fields(field1, field2) {
    total = create_field()
    for(var i=0; i<10; i++) {
        for(var j=0; j<10; j++) {
            total[i][j] = field1[i][j] + field2[i][j]
        }
    }
    return total
}

total = add_fields(field1, field2)

console.log(total)
console.log(total)