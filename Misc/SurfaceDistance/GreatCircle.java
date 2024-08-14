public class GreatCircle {

    //notes
    //The goal of this program is to calculate the ground
    //distance between two coordinate points on earth


    public static void main(String[] args) {
        // initializes constants and command line arguments
        double r = 6371.0;
        double x1 = Math.toRadians(Double.parseDouble(args[0]));
        double y1 = Math.toRadians(Double.parseDouble(args[1]));
        double x2 = Math.toRadians(Double.parseDouble(args[2]));
        double y2 = Math.toRadians(Double.parseDouble(args[3]));

        // calculates the spherical distance of the two points
        double distance = 2 * r * Math.asin(Math.sqrt(
                Math.pow(Math.sin(0.5 * (x2 - x1)), 2) +
                        Math.cos(x1) * Math.cos(x2) *
                                Math.pow(Math.sin(0.5 * (y2 - y1)), 2)));
        // prints the distance in the desired format
        System.out.println(distance + " kilometers");
    }
}
