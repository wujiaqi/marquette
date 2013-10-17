/*axioms*/

female(mum).
female(kydd).
female(elizabeth).
female(margaret).
female(diana).
female(anne).
female(sarah).
female(sophie).
female(zara).
female(beatrice).
female(eugenie).
male(george).
male(spencer).
male(philip).
male(charles).
male(mark).
male(andrew).
male(edward).
male(william).
male(harry).
male(peter).
male(louise).
male(james).

child(elizabeth, mum).
child(elizabeth, george).
child(margaret, mum).
child(margaret, george).
child(diana, spencer).
child(diana, kydd).
child(charles, elizabeth).
child(charles, philip).
child(anne, elizabeth).
child(anne, philip).
child(andrew, elizabeth).
child(andrew, philip).
child(edward, elizabeth).
child(edward, philip).
child(william, diana).
child(william, charles).
child(harry, diana).
child(harry, charles).
child(peter, anne).
child(peter, mark).
child(zara, anne).
child(zara, mark).
child(beatrice, andrew).
child(beatrice, sarah).
child(eugenie, andrew).
child(eugenie, sarah).
child(louise, edward).
child(louise, sophie).
child(james, edward).
child(james, sophie).

married(george, mum).
married(mum, george).
married(spencer, kydd).
married(kyddd, spencer).
married(elizabeth, philip).
married(philip, elizabeth).
married(diana, charles).
married(charles, diana).
married(anne, mark).
married(mark, anne).
married(andrew, sarah).
married(sarah, andrew).
married(edward, sophie).
married(sophie, edward).

grandChild(X, Y):-child(X, Z), child(Z, Y).
greatGrandChild(X, Y):-child(X, A), child(A, B), child(B, Y).
greatGrandParent(X, Y):-greatGrandChild(Y, X).
ancestor(X, Y):-child(Y, X); (child(Y, B), ancestor(X, B)).

sibling(X, Y):-child(X, A), child(Y, A), X \= Y.
brother(X, Y):-sibling(X, Y), male(X).
sister(X, Y):-sibling(X, Y), female(X).

daughter(X, Y):-child(X, Y), female(X).
son(X, Y):-child(X, Y), male(X).
firstCousin(X, Y):-grandChild(X, A), grandChild(Y, A), not(sibling(X, Y)), X \= Y.
siblingInLaw(X, Y):-sibling(X, B), married(B, Y).
brotherInLaw(X, Y):-siblingInLaw(X, Y), male(X).
sisterInLaw(X, Y):-siblingInLaw(X, Y), female(X).
pibling(X, Y):-child(Y, A), (sibling(A, X); siblingInLaw(A, X)).
aunt(X, Y):-pibling(X, Y), female(X).
uncle(X, Y):-pibling(X, Y), male(X).
