function create_field() {
    var field = []
    for (var i = 0; i < 10; i++) {
        field.push(new Array(10).fill(0))
    }
    return field
}

function create_boats() {
    return [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
}


function add_fields(field1, field2) {
    total = create_field()
    for (var i = 0; i < 10; i++) {
        for (var j = 0; j < 10; j++) {
            total[i][j] = field1[i][j] + field2[i][j]
        }
    }
    return total
}

function sum_field(field) {
    var sum = 0;
    for (var i = 0; i < 10; i++) {
        for (var j = 0; j < 10; j++) {
            sum += field[i][j]
        }
    }
    return sum
}

function getRandomInt(x) {
    return Math.floor(Math.random() * x);
}

function copy_array(arr) {
    return JSON.parse(JSON.stringify(arr));
}

function add_boat(field, boat_length) {
    var out = copy_array(field)
    var row = getRandomInt(10)
    var col = getRandomInt(10)
    var direction = getRandomInt(2)
    if (direction === 0) {
        if (row + boat_length > 9) {
            add_boat(field, boat_length)
        } else {
            for (var inc_row = 0; inc_row < boat_length; inc_row++) {
                out[row + inc_row][col] = 5
            }
        }
    } else if (direction === 1) {
        if (col + boat_length > 9) {
            add_boat(field, boat_length)
        } else {
            for (var inc_col = 0; inc_col < boat_length; inc_col++) {
                out[row][col + inc_col] = 5
            }
        }
    }
    return out
}

field1 = create_field()
field2 = create_field()
boats1 = create_boats()
boats2 = create_boats()

field1 = add_boat(field1, 3)
field2 = add_boat(field2, 4)

total = add_fields(field1, field2)
sum1 = sum_field(total)


console.log(sum1)
console.log(total)
console.log(sum1)