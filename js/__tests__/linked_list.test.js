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

