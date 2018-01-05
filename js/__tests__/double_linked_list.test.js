let dll = require(../double_linked_list)

test('Test there is no data on initialization', () => {
    let d = new dll.Dll();
    expect(d.head).toBeNull();
});

test('Test push method works', () => {
    let d = new dll.Dll();
    d.push(99)
    d.push(88)
    expect(d.head.val).toBe(88)
    expect(d.head.next.val)toBe(99)
});

test('Test input as iterable', () => {
    let d = new dll.Dll([99, 98]);
    expect(d.head.val).toBe(98)
    expect(d.head.next.val)toBe(99)
});

test('Test pop method works', () => {
    let d = new dll.Dll([99, 98]);
    expect(d.pop()).toBe(99)
    expect(d.head.val).toBe(98)
});

test('Test pop method on empty linked list', () => {
    let d = new dll.Dll();
    expect(d.pop()).toBeNull()
});

test('Test shift method works', () => {
    let d = new dll.Dll([99, 98, 97, 96]);
    expect(d.shift()).toBe(96)
})

test('Test append method works', () => {
    let d = new dll.Dll([99, 98, 97, 96]);
    d.append(88)
    expect(d.shift()).toBe(88)
})

test('Test remove method', () => {
    let d = new dll.Dll([99, 98, 97, 96]);
    d.remove(97)
    expect(d.size()).toBe(3)
})