function variance = Heter( BA )
L = load('C:/Users/Administrator/Desktop/��ҵ����/��籨��/L.txt');
IL = transpose(sum(L));
IB = sum(L,2);
N = size(L,1);
p = 0.8;
variance = (BA - sum(IL) / p / N) .^2;
variance = sum(variance) / N;
end