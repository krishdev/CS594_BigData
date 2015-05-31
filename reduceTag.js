
function reduce1(key,values) {

            //return   Array.sum(value);
	return values.length;
  
}

function count(values) {

    values.sort( function(a,b) {return a - b;} );

    var half = Math.floor(values.length/2);

    if(values.length % 2)
        return values[half];
    else
        return (values[half-1] + values[half]) / 2.0;
}

function mode(values){
     if(values.length == 0)
    	return null;
    var modeMap = {};
    var maxEl = values[0], maxCount = 1;
    for(var i = 0; i < values.length; i++)
    {
    	var el = values[i];
    	if(modeMap[el] == null)
    		modeMap[el] = 1;
    	else
    		modeMap[el]++;
    	if(modeMap[el] > maxCount)
    	{
    		maxEl = el;
    		maxCount = modeMap[el];
    	}
    }
    print("reduce:", values, " \t", maxEl);
    return maxEl;
}

function variance(values){
     var len = 0;
    var sum=0;
    for(var i=0;i<values.length;i++)
    {
             len = len + 1;
             sum = sum + parseFloat(values[i]);

    }

    var v = 0;
    if (len > 1)
    {
        var mean = sum / len;
        for(var i=0;i<values.length;i++)
        {
              if (values[i] == ""){}
              else
              {
                  v = v + (values[i] - mean) * (values[i] - mean);
              }
        }

        return v / len;
    }
    else
    {
         return 0;
    }
}

//Get the largest number of a number array
function max(values)
{
    var max = -99999;

    for(var i=0;i<values.length;i++)
    {

             if (i == 0) {max = values[i];}
             else if (max < values[i]) {max = values[i];}

    }

    return max;
}

//Get the smallest number of a number array
function min(arr)
{
    var min = 99999;

    for(var i=0;i<arr.length;i++)
    {

             if (i == 0) {min = arr[i];}
             else if (min > arr[i]) {min = arr[i];}

    }

    return min;
}

