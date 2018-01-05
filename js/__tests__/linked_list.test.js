let linkedList = require(../linked_list)

test('Test there is no data on initialization', () => {
    let l = new linkedList.LinkedList();
    expect(l.head).toBeNull();
});

test('Test push method works', () => {
    let l = new linkedList.LinkedList();
    l.push(99)
    l.push(88)
    expect(l.head.val).toBe(88)
    expect(l.head.next.val)toBe(99)
});

test('Test input as iterable', () => {
    let l = new linkedList.LinkedList([99, 98]);
    expect(l.head.val).toBe(98)
    expect(l.head.next.val)toBe(99)
});

test('Test pop method works', () => {
    let l = new linkedList.LinkedList([99, 98]);
    expect(l.pop()).toBe(99)
    expect(l.head.val).toBe(98)
});

test('Test pop method on empty linked list', () => {
    let l = new linkedList.LinkedList();
    expect(l.pop()).toBeNull()
});
