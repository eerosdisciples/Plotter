
fileID = fopen('particle.csv');

formatSpec = '%f %f %f %f %f %f %f'; %flyttal

DATA=textscan(fileID,formatSpec,'HeaderLines',1,'delimiter',',','CollectOutput',1); % data till cell

fclose('all');

data = cell2mat(DATA); % cell till matris
X = data(:,2); 
Y = data(:,3) ;
Z =  data(:,4);

clf
plot3(X,Y,Z);
set(gca, 'XDir', 'reverse')
xlabel('x [m]')
ylabel('y [m]')
zlabel('z [m]')
grid on


%%
plot(sqrt(X.^2+Y.^2),Z)
xlabel('r [m]')
ylabel('z [m]')


