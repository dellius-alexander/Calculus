#!/usr/bin/env bash
#set -e : Exit the shell script if any statement returns a non-true return value.
#set -u : Treat unset variables and parameters other than the special parameters ‘@’ or ‘*’ as an error when performing parameter expansion.
#set -o pipefail : If set, the return value of a pipeline is the value of the last (rightmost) command to exit with a non-zero status, or zero if all commands in the pipeline exit successfully.
#set -x : Print commands and their arguments as they are executed.
#set -euxo pipefail : The set -x option will print the command being executed before the shell executes it. The -u option causes the shell to treat unset variables as an error and exit immediately. The -o pipefail option causes a pipeline to return the exit status of the last command in the pipe that returned a non-zero return value.
#set -a : Mark variables which are modified or created for export.
#set -F : Disable pathname expansion.

# command execution usage function
usage() {
  echo """Usage: ${0} <url> <destination> <checksum>"""
  exit 1
}

# main function
main(){  # Start of main function
  # install try catch
  set -eo pipefail # Exit the shell script if any statement returns a non-true return value.

  local URL_REGEX=".*(http(s)?)://.*"
  local CHECKSUM_REGEX=".*(sha[0-9]+)-.*"
  # Test fd1, if it is not empty and is a url address
  local URL=$(if [ ! -z "${1}" ] && [[ "${1}" =~ ${URL_REGEX:-""} ]]; then echo "${1}"; else echo 'Null'; fi && wait $!) && wait $!
  # Get the file name for the URL
  local FILENAME=$(if [ ! -z "${1}" ] && [[ "${1}" =~ ${URL_REGEX:-""} ]]; then echo "${1##*/}"; else echo 'Null'; fi && wait $!) && wait $!
  # Test fd2, if it is not empty and that the destination path is a directory
  local DEST=$(if [ -s "${2}" ] && [ -d "${2}" ]; then echo "${2}"; else echo 'Null'; fi && wait $!) && wait $!
  # Test fd3, if it is not empty and is the integrity checksum for the download, we also strip the checksum identifier form the front of the hash
  local ALGORITHM=$(if [ ! -z "${3}" ] && [[ "${3}" =~ ${CHECKSUM_REGEX} ]]; then echo "${3}" | cut -d '-' -f 1 ; else echo 'Null'; fi && wait $!) && wait $!
  # Get CHECKSUM string from fd3
  local CHECKSUM=$(if [ ! -z "${3}" ] && [[ "${3}" =~ ${CHECKSUM_REGEX} ]]; then echo "${3}" ; else echo 'Null'; fi && wait $!) && wait $!
  echo """Variables: [${URL}, ${DEST}, ${ALGORITHM}, ${CHECKSUM}]"""
  #local PROPERTIES=(['url']="${URL}" ['dest']="${DEST}" ['algorithm']="${ALGORITHM}" ['checksum']="${CHECKSUM}") && wait $!
  local PROPERTIES=("${URL}" "${FILENAME}" "${DEST}" "${ALGORITHM}" "${CHECKSUM}") && wait $!
  local INTEGRITY_CHECK
  # Print all the array elements
  for key in "${!PROPERTIES[@]}"; do
      printf "PROPERTIES[%s]=%s\n" "$key" "${PROPERTIES[$key]}"
      sleep 0.5
  done
  printf "Property Count: %s\n" "${#PROPERTIES[@]}"
  # Test if all the required properties are set
  if [ "${#PROPERTIES[@]}" -ne 5 ]; then
      echo "Not all required properties are set"
      usage
  fi
  sleep 1
  # Test if the destination directory exists and download the file
  if [ ! -d "${PROPERTIES[2]}" ]; then
      echo "Destination directory does not exist"
      usage
  else
      echo "Destination directory exists"
      echo "Downloading file ......"
      # Download the file
      if curl -o "${PROPERTIES[2]}/${PROPERTIES[1]}" "${PROPERTIES[0]}" 2>&1 ; then
          echo "Downloaded file successfully"
          ls -l "${PROPERTIES[2]}/${PROPERTIES[1]}"
          INTEGRITY_CHECK="${PROPERTIES[3]}-$(openssl dgst -${PROPERTIES[3]} -binary "${PROPERTIES[2]}/${PROPERTIES[1]}" | openssl base64 -A)" && wait $!
          echo "Integrity check: ${INTEGRITY_CHECK}"
      else
          echo "Downloaded file failed" >&2
          echo $?
          exit 1
      fi
  fi
  sleep 1
  # Test the integrity of the downloaded file
  if [ ! -z "${PROPERTIES[3]}" ] && [ ! -z "${PROPERTIES[4]}" ]; then
      echo "Integrity check is set"
      # Test if the checksum matches the downloaded file
      if [[ "${PROPERTIES[4]}" =~ "${INTEGRITY_CHECK}" ]] ; then
          echo "Integrity check passed"
      else
          echo "Integrity check failed"
          echo "Deleting file ......"
          # delete the file
          rm "${PROPERTIES[2]}/${PROPERTIES[1]}" 2>&1
          exit 1
      fi
  else
      echo "Integrity check is not set"
      echo "Deleting file ......"
      # delete the file
      rm "${PROPERTIES[2]}/${PROPERTIES[1]}" 2>&1
      exit 1
  fi
  echo "Done"
  #
  #set +u
}  # End of main function
# reset the environment before set command
#########################################################################################
#main "https://cdn.jsdelivr.net/npm/@popperjs/core@2.10.2/dist/umd/popper.min.js" \
#"/tmp" \
#"sha384-7+zCNj/IqJ95wo16oMtfsKbZ9ccEh31eOz1HGyDuCQ6wgnyJNSYdrPa03rtR1zdB" && wait $!
#########################################################################################
#main 'https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.min.js' \
#"/tmp" \
#"sha384-QJHtvGhmr9XOIpI6YVutG+2QOK9T+ZnN4kzFN1RtK3zEFEIsxhlmWl5/YESvpZ13" && wait $!
#########################################################################################
main "${1}" "${2}" "${3}" && wait $!