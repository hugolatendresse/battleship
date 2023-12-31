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

function max_field(field) {
    var max = -1;
    for (var i = 0; i < 10; i++) {
        for (var j = 0; j < 10; j++) {
            if (max < field[i][j]) {
                max = field[i][j]
            }
        }
    }
    return max
}


function getRandomInt(x) {
    return Math.floor(Math.random() * x);
}

function copy_array(arr) {
    return JSON.parse(JSON.stringify(arr));
}

function add_boat(field, boat_length) {
    console.log(field.length)
    var boat_field = create_field()
    var row = getRandomInt(10)
    var col = getRandomInt(10)
    var direction = getRandomInt(2)
    if (direction === 0) {
        if (row + boat_length > 9) {
            return add_boat(field, boat_length)
        } else {
            for (var inc_row = 0; inc_row < boat_length; inc_row++) {
                boat_field[row + inc_row][col] = 5
            }
        }
    } else if (direction === 1) {
        if (col + boat_length > 9) {
            return add_boat(field, boat_length)
        } else {
            for (var inc_col = 0; inc_col < boat_length; inc_col++) {
                boat_field[row][col + inc_col] = 5
            }
        }
    }
    var out = add_fields(boat_field, copy_array(field))
    if (max_field(out) === 5) {
        // TODO: can't allow two boats to touch either, even diagonally
        console.log(out.length)
        return out
    } else {
        console.log(field.length)
        return add_boat(field, boat_length)
    }
}

function add_all_boats(field, boats) {
    for (var i = 0; i < boats.length; i++) {
        field = add_boat(field, boats[i])
    }
    return field
}

field1 = create_field()
field2 = create_field()
boats1 = create_boats()
boats2 = create_boats()
field1 = add_all_boats(field1, boats1)
field2 = add_all_boats(field2, boats2)
console.log(field1)
console.log(field2)




// TODO: can't allow two boats to touch, even diagonally

console.log(total)
