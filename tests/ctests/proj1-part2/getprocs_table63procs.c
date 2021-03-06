#include "types.h"
#include "stat.h"
#include "user.h"
//#include "ProcessInfo.h"
//#include "processinfo.h"
//#include "processInfo.h"

void
test_failed()
{
  printf(1, "TEST FAILED\n");
  exit();
}

void
test_passed()
{
 printf(1, "TEST PASSED\n");
 exit();
}

void
checkNumeric(char* name, int expected, int actual)
{
  if(expected != actual){
    printf(1, "%s  expected: %d, actual: %d\n", name, expected, actual);
    test_failed();
  }
}

void
checkString(char* name, char* expected, char* actual)
{
  int i = 0;
  while(i < 16){
    if(expected[i] != actual[i]){
      printf(1, "%s  expected: %s, actual: %s\n", name, expected, actual);
      test_failed();
    }
    i++;
    if(expected[i] == '\0' && actual[i] == '\0'){
      break;
    }
  }
}

int
main(int argc, char *argv[])
{
  int pid;
  int i;
  int numForks = 60;
  for(i = 0; i < numForks; i++){
    pid = fork();
    if(pid != 0){
      break;
    } else {
      if(i == numForks - 1){
        struct ProcessInfo processInfoTable[64];
  printf(1, "table address: %p\n", processInfoTable);
        getprocs(processInfoTable);

        checkNumeric("processInfoTable[0].pid", 1, processInfoTable[0].pid);
        checkNumeric("processInfoTable[0].state", 2, processInfoTable[0].state);
        checkNumeric("processInfoTable[0].sz", 12288, processInfoTable[0].sz);
        checkString("processInfoTable[0].name", "init", processInfoTable[0].name);

        checkNumeric("processInfoTable[1].pid", 2, processInfoTable[1].pid);
        checkNumeric("processInfoTable[1].ppid", 1, processInfoTable[1].ppid);
        checkNumeric("processInfoTable[1].state", 2, processInfoTable[1].state);
        checkNumeric("processInfoTable[1].sz", 16384, processInfoTable[1].sz);
        checkString("processInfoTable[1].name", "sh", processInfoTable[1].name);

        int j;
        for(j = 3; j < numForks+3; j++){
          checkNumeric("processInfoTable[i].pid", j, processInfoTable[j-1].pid);
          checkNumeric("processInfoTable[i].ppid", j-1, processInfoTable[j-1].ppid);
          checkNumeric("processInfoTable[i].state", 2, processInfoTable[j-1].state);
          checkNumeric("processInfoTable[i].sz", 16384, processInfoTable[j-1].sz);
          checkString("processInfoTable[i].name", "usertests", processInfoTable[j-1].name);
        }

        checkNumeric("processInfoTable[62].pid", 63, processInfoTable[62].pid);
        checkNumeric("processInfoTable[62].ppid", 62, processInfoTable[62].ppid);
        checkNumeric("processInfoTable[62].state", 4, processInfoTable[62].state);
        checkNumeric("processInfoTable[62].sz", 16384, processInfoTable[62].sz);
        checkString("processInfoTable[62].name", "usertests", processInfoTable[62].name);

        test_passed();
      }
    }
  }
  wait();
  exit();
  return 0;
}
