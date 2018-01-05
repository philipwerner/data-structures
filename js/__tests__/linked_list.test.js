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

test('Test size method', () => {
    let l = new linkedList.LinkedList([99, 98, 97, 96]);
    expect(l.size()).toBe(4)
})

test('Test size after pop', () => {
    let l = new linkedList.LinkedList([99, 98, 97, 96]);
    l.pop()
    expect(l.size()).toBe(3)
})

test('Test search method', () => {
    let l = new linkedList.LinkedList([99, 98, 97, 96]);
    expect(l.search(97).val).toBe(97)
})

test('Test search method when node not present', () => {
    let l = new linkedList.LinkedList([99, 98, 97, 96]);
    expect(l.search(79).val).toBeNull()
})

test('Test remove method', () => {
    let l = new linkedList.LinkedList([99, 98, 97, 96]);
    l.remove(97)
    expect(l.size()).toBe(3)
    expect(l.display()).toBe('(96, 98, 99)')
})

test('Test display method', () => {
    let l = new linkedList.LinkedList([99, 98, 97, 96]);
    expect(l.display()).toBe('(96, 97, 98, 99)')
})