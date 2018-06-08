clc;
filename = VideoReader('traffic.avi');
implay('traffic.avi')
darkcar = rgb2gray(read(filename,71));
subplot(2,2,1);
imshow(darkcar);
title('original frame');

darkcarvalue = 50;
nodarkcar = imextendedmax(darkcar, darkcarvalue);
subplot(2,2,2);
imshow(nodarkcar);
title('removed black car');

disk = strel('disk', 2);
removestructures = imopen(nodarkcar,disk);
subplot(2,2,3);
imshow(removestructures);
title('morphed image');


nframes = get(filename, 'NumberOfFrames');
I = read(filename, 1);
taggedCars = zeros([size(I,1) size(I,2) 3 nframes], class(I));

for k = 1 : nframes
    singleFrame = read(filename, k);
    %imwrite(singleFrame, ['Image' int2str(k), '.jpg']);
    %im(k) =image(singleFrame);
    
    % Convert to grayscale to do morphological processing.
    I = rgb2gray(singleFrame);

    % Remove dark cars.
    nodarkcar = imextendedmax(I, darkcarvalue);

    % Remove lane markings and other non-disk shaped structures.
    removestructures = imopen(nodarkcar, disk);

    % Remove small structures.
    %
    removesmallstructures = bwareaopen(removestructures, 150);

    % Get the area and centroid of each remaining object in the frame. The
    % object with the largest area is the light-colored car.  Create a copy
    % of the original frame and tag the car by changing the centroid pixel
    % value to red.
    taggedCars(:,:,:,k) = singleFrame;

    stats = regionprops(removesmallstructures, {'Centroid','Area'});
    if ~isempty([stats.Area])
        areaArray = [stats.Area];
        [junk,idx] = max(areaArray);
        c = stats(idx).Centroid;
        c = floor(fliplr(c));
        width = 2;
        row = c(1)-width:c(1)+width;
        col = c(2)-width:c(2)+width;
        taggedCars(row,col,1,k) = 255; %red color
        taggedCars(row,col,2,k) = 0; %green color
        taggedCars(row,col,3,k) = 180;%blue color
    end
end

frameRate = get(filename,'FrameRate');
implay(taggedCars,frameRate);

