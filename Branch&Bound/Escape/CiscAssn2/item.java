package CiscAssn2;
//Hassan Haq
//10061306
//12huh
//used to make objects of items
public class item {
	int value;
	int mass;
	double ratio;
	int index;
	public item(int value, int mass, int index){
		this.value = value;
		this.mass = mass;
		this.ratio = (double)value/mass;
		this.index = index;
	}
}
