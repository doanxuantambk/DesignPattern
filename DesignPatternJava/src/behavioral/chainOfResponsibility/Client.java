package behavioral.chainOfResponsibility;

public class Client {
    public static void main(String[] args) {
        Logger logger = AppLogger.getLogger();
        logger.log(LogLevel.DEBUG, "Debug message");
        System.out.println();
        logger.log(LogLevel.ERROR, "Error message");
        System.out.println();
        logger.log(LogLevel.FATAL, "Fatal message");
    }
}
