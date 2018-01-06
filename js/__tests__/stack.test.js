let stack = require(../stack)

test('Test there is no data on initialization', () => {
    let s = new stack.Stack();
    expect(l.head).toBeNull();
});

test('Test push method works', () => {
    let s = new stack.Stack();
    s.push(25)
    s.push(50)
    expect(s.head.val).toBe(50)
    expect(s.head.next.val)toBe(25)
});